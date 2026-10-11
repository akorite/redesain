import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, sys
sys.path.insert(0,'/Users/devin/textbook-ml/code/ch08')
from optim_scratch import run, init, loss_acc, fwd, grads
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
X,y = load_digits(return_X_y=True); X=X/16.
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=.25,random_state=7,stratify=y)

# 1. four-optimizer loss curves
fig,ax=plt.subplots(figsize=(5.8,3))
for nm,mo,lr,c in [('GD full-batch','gd',.5,'gray'),('SGD B=64','sgd',.05,'b'),
                   ('SGD+momentum','mom',.05,'g'),('Adam','adam',.01,'r')]:
    tr,_=run(mo,lr); ax.plot(tr,color=c,lw=1.5,label=nm)
ax.set_xlabel('epoch');ax.set_ylabel('train loss');ax.legend();ax.grid(alpha=.3)
fig.tight_layout();fig.savefig('ch08/optim_race.pdf');plt.close(fig)

# 2. lr triptych on momentum
fig,axes=plt.subplots(1,3,figsize=(10,2.6),sharey=True)
for ax,lr,tt in zip(axes,[0.001,0.05,1.0],['too slow ($\\eta$=0.001)','good ($\\eta$=0.05)','too high ($\\eta$=1.0)']):
    P=init();n=len(Xtr);mom=[np.zeros_like(w) for w in P];tr=[]
    for ep in range(30):
        idx=np.random.default_rng(ep).permutation(n)
        for s in range(0,n,64):
            G=grads(P,Xtr[idx[s:s+64]],ytr[idx[s:s+64]])
            for i in range(4): mom[i]=.9*mom[i]-lr*G[i];P[i]+=mom[i]
        tr.append(loss_acc(P,Xtr,ytr)[0])
    ax.plot(tr,'k-',lw=1.4);ax.set_title(tt,fontsize=9);ax.grid(alpha=.3)
    ax.set_xlabel('epoch')
axes[0].set_ylabel('train loss');axes[0].set_ylim(0,3)
fig.tight_layout();fig.savefig('ch08/lr_triptych.pdf');plt.close(fig)

# 3. activation histograms bad vs kaiming init
fig,axes=plt.subplots(1,2,figsize=(8.5,2.6),sharey=True)
for ax,(mode,tt) in zip(axes,[('bad','N(0,1) init'),('kaiming','Kaiming init')]):
    rng=np.random.default_rng(7);d,h,C=64,48,10
    s1,s2=(1.0,1.0) if mode=='bad' else (np.sqrt(2/d),np.sqrt(2/h))
    W1=rng.normal(0,s1,(d,h));W2=rng.normal(0,s2,(h,C))
    z1=Xtr@W1;a1=np.maximum(0,z1);z2=a1@W2
    ax.hist(z1.ravel(),bins=60,alpha=.7,color='b',label='$z_1$')
    ax.hist(z2.ravel(),bins=60,alpha=.7,color='r',label='$z_2$')
    ax.set_title(tt,fontsize=9);ax.legend(fontsize=7);ax.set_xlim(-8,8)
axes[0].set_ylabel('count')
fig.tight_layout();fig.savefig('ch08/init_hist.pdf');plt.close(fig)

# 4. schedule shapes
fig,ax=plt.subplots(figsize=(6,2.6))
ep=np.arange(200)
step=np.where(ep<70,1.,np.where(ep<140,.1,.01))
cos=.5*(1+np.cos(np.pi*ep/199))
warm=np.minimum(ep/19+1e-9,1.)*cos
ax.plot(ep,step,'k-',lw=1.4,label='step')
ax.plot(ep,cos,'b--',lw=1.4,label='cosine')
ax.plot(ep,warm,'r-.',lw=1.4,label='warmup+cosine')
ax.set_xlabel('epoch');ax.set_ylabel('$\\eta_t/\\eta_0$');ax.legend();ax.grid(alpha=.3)
fig.tight_layout();fig.savefig('ch08/schedules.pdf');plt.close(fig)

# 5. gradient norm dashboard: real run w/ momentum
P=init();n=len(Xtr);mom=[np.zeros_like(w) for w in P]
g1=[];g2=[];ls=[]
for ep in range(60):
    idx=np.random.default_rng(ep).permutation(n)
    for s in range(0,n,64):
        G=grads(P,Xtr[idx[s:s+64]],ytr[idx[s:s+64]])
        g1.append(np.linalg.norm(G[0]));g2.append(np.linalg.norm(G[2]))
        for i in range(4):mom[i]=.9*mom[i]-.05*G[i];P[i]+=mom[i]
    ls.append(loss_acc(P,Xtr,ytr)[0])
fig,(a1,a2)=plt.subplots(1,2,figsize=(9,2.6))
a1.plot(ls,'k-');a1.set_title('loss per epoch',fontsize=9);a1.set_xlabel('epoch')
a2.plot(g1,'b-',lw=.6,label='||dW1||');a2.plot(g2,'r-',lw=.6,label='||dW2||')
a2.set_title('gradient norms per step',fontsize=9);a2.set_xlabel('step');a2.legend(fontsize=7)
for a in (a1,a2): a.grid(alpha=.3)
fig.tight_layout();fig.savefig('ch08/grad_dashboard.pdf');plt.close(fig)

# 6. 2-D loss surface trajectories: tiny 2-param quadratic
A=np.array([[4.,0.],[0.,0.4]])
def f(w): return .5*w@A@w
def g(w): return A@w
w0=np.array([2.4,2.4])
def traj(mode,steps,lr):
    w=w0.copy();v=np.zeros(2);path=[w.copy()]
    for _ in range(steps):
        if mode=='gd': w-=lr*g(w)
        elif mode=='mom': v=.9*v-lr*g(w);w+=v
        elif mode=='nag': v0=v.copy();v=.9*v-lr*g(w+.9*v);w+=v
        path.append(w.copy())
    return np.array(path)
xx,yy=np.meshgrid(np.linspace(-3,3,300),np.linspace(-3,3,300))
Z=.5*(4*xx**2+.4*yy**2)
fig,ax=plt.subplots(figsize=(5,4))
ax.contour(xx,yy,Z,levels=12,cmap='gray',alpha=.6)
for mo,c,nm in [('gd','b','GD'),('mom','r','momentum'),('nag','g','Nesterov')]:
    P=traj(mo,25,.12);ax.plot(*P.T,'.-',color=c,lw=1,ms=4,label=nm)
ax.plot(*w0,'ko',ms=7);ax.plot(0,0,'k*',ms=12)
ax.set_xlabel('$w_1$');ax.set_ylabel('$w_2$');ax.legend(fontsize=8)
fig.tight_layout();fig.savefig('ch08/surface_traj.pdf');plt.close(fig)
print("all figs done")
