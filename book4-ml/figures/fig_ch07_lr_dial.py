import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
X,y = load_digits(return_X_y=True); X=X/16.
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=.25,random_state=7,stratify=y)
def run(lr,seed=7):
    rng=np.random.default_rng(seed); d,h,C=64,48,10
    W1=rng.normal(0,np.sqrt(2/d),(d,h));b1=np.zeros(h)
    W2=rng.normal(0,np.sqrt(2/h),(h,C));b2=np.zeros(C)
    losses=[]
    for ep in range(60):
        z1=Xtr@W1+b1; a1=np.maximum(0,z1); z2=a1@W2+b2
        z2-=z2.max(1,keepdims=True); e=np.exp(z2); p=e/e.sum(1,keepdims=True)
        losses.append(-np.log(p[np.arange(len(ytr)),ytr]+1e-12).mean())
        dz=p.copy(); dz[np.arange(len(ytr)),ytr]-=1; dz/=len(ytr)
        dW2=a1.T@dz; db2=dz.sum(0); da=dz@W2.T; dz1=da*(z1>0)
        dW1=Xtr.T@dz1; db1=dz1.sum(0)
        for W,g in [(W1,dW1),(b1,db1),(W2,dW2),(b2,db2)]: W-=lr*g
    return losses
fig,ax=plt.subplots(figsize=(5.6,2.8))
for lr,c in [(0.05,'k'),(0.5,'r'),(2.0,'b')]:
    L=run(lr); ax.plot(L,color=c,lw=1.5,label=f"lr={lr}")
ax.set_ylim(0,6);ax.set_xlabel("epoch");ax.set_ylabel("train loss")
ax.legend();ax.grid(alpha=.3)
fig.tight_layout();fig.savefig("ch07/lr_dial.pdf")
