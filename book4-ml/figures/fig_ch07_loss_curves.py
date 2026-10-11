import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
X,y=load_digits(return_X_y=True);X=X/16.
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=7,stratify=y)
rng=np.random.default_rng(7);d,h,C=64,48,10
W1=rng.normal(0,np.sqrt(2/d),(d,h));b1=np.zeros(h)
W2=rng.normal(0,np.sqrt(2/h),(h,C));b2=np.zeros(C)
tr=[];te=[]
for ep in range(60):
    z1=Xtr@W1+b1;a1=np.maximum(0,z1);z2=a1@W2+b2
    z2-=z2.max(1,keepdims=True);e=np.exp(z2);p=e/e.sum(1,keepdims=True)
    tr.append(-np.log(p[np.arange(len(ytr)),ytr]+1e-12).mean())
    q1=Xte@W1+b1;q2=np.maximum(0,q1)@W2+b2
    q2-=q2.max(1,keepdims=True);e2=np.exp(q2);p2=e2/e2.sum(1,keepdims=True)
    te.append(-np.log(p2[np.arange(len(yte)),yte]+1e-12).mean())
    dz=p.copy();dz[np.arange(len(ytr)),ytr]-=1;dz/=len(ytr)
    dW2=a1.T@dz;db2=dz.sum(0);da=dz@W2.T;dz1=da*(z1>0)
    dW1=Xtr.T@dz1;db1=dz1.sum(0)
    for W,g in [(W1,dW1),(b1,db1),(W2,dW2),(b2,db2)]:W-=.5*g
fig,ax=plt.subplots(figsize=(5.4,2.8))
ax.plot(tr,'k-',lw=1.6,label='train');ax.plot(te,'r--',lw=1.6,label='test')
ax.set_xlabel('epoch');ax.set_ylabel('cross-entropy');ax.legend();ax.grid(alpha=.3)
fig.tight_layout();fig.savefig('ch07/loss_curves.pdf')
