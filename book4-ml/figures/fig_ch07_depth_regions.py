import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
X,y = make_moons(n_samples=400,noise=.25,random_state=4)
xmin,xmax=X[:,0].min()-.3,X[:,0].max()+.3
ymin,ymax=X[:,1].min()-.3,X[:,1].max()+.3
xx,yy=np.meshgrid(np.linspace(xmin,xmax,300),np.linspace(ymin,ymax,300))
g=np.c_[xx.ravel(),yy.ravel()]
fig,axes=plt.subplots(1,4,figsize=(11,2.5))
ms=[("logistic (0 hid)",None),("1 layer x16",(16,)),
    ("2 layers x16",(16,16)),("3 layers x16",(16,16,16))]
for ax,(nm,hl) in zip(axes,ms):
    m=(LogisticRegression().fit(X,y) if hl is None else
       MLPClassifier(hidden_layer_sizes=hl,max_iter=2000,random_state=0).fit(X,y))
    ax.contourf(xx,yy,m.predict(g).reshape(xx.shape),levels=[-.5,.5,1.5],
                colors=['#f4c7c3','#c7dbf0'],alpha=.9)
    ax.scatter(*X[y==0].T,c='#c0392b',s=6); ax.scatter(*X[y==1].T,c='#2166ac',s=6)
    ax.set_title(nm,fontsize=8); ax.set_xticks([]);ax.set_yticks([])
fig.tight_layout();fig.savefig("ch07/depth_regions.pdf")
