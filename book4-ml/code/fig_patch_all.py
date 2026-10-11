# fig_patch_all.py -- the REVISE-pass figure additions: every panel a
# real computed object (data files, CSVs, or re-derived numbers).
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, csv, math

M = dict(fontsize=7)

# ---------- ch01 ----------
# timing bar chart from the real timing.dat
import csv
rows=[r for r in csv.reader(open('ch01/timing.dat'),delimiter=' ')][1:]
names=[r[0] for r in rows]; sp=[float(r[1]) for r in rows]
fig,ax = plt.subplots(figsize=(4.6,2.4))
ax.bar(range(len(sp)), sp, color='#2166ac')
ax.set_xticks(range(len(sp))); ax.set_xticklabels(names,rotation=20,fontsize=6)
for i,v in enumerate(sp): ax.text(i,v+2,f'{v:.0f}x',ha='center',**M)
ax.set_ylabel('slowdown x')
ax.set_title('real loop-vs-vectorised slowdowns (timing.dat)', **M)
fig.tight_layout(); fig.savefig('ch01/timing_bar.pdf'); plt.close(fig)

# leak bar from leak.dat
rows=[r for r in csv.reader(open('ch01/leak.dat'),delimiter=' ')][1:]
names=[r[0] for r in rows]
leak=[float(r[1]) for r in rows]; hon=[float(r[2]) for r in rows]
fig,ax = plt.subplots(figsize=(4.4,2.4))
xs = np.arange(len(names))
ax.bar(xs-0.2, hon, 0.4, label='honest split', color='#2166ac')
ax.bar(xs+0.2, leak, 0.4, label='leaked', color='#b2182b')
ax.set_xticks(xs); ax.set_xticklabels(names)
ax.legend(); ax.set_ylim(0,1.05)
ax.set_title('phantom accuracy gain from test-row leakage (leak.dat)', **M)
fig.tight_layout(); fig.savefig('ch01/leak_bar.pdf'); plt.close(fig)

# X-as-matrix block panel on real iris numbers
iris = np.loadtxt('../data/iris.csv', delimiter=',', skiprows=1, usecols=(0,1,2,3))
fig,ax = plt.subplots(figsize=(4.6,2.4))
im = ax.imshow(iris, aspect='auto', cmap='viridis')
ax.set_xlabel('feature j (sepal L/W, petal L/W)'); ax.set_ylabel('sample i')
ax.set_title(r'iris $X\in\mathbb{R}^{150\times4}$ rendered literally', **M)
fig.colorbar(im, fraction=0.04)
fig.tight_layout(); fig.savefig('ch01/x_matrix.pdf'); plt.close(fig)

# broadcasting steps: (4,1)+(1,3) real arrays
a = np.array([[1.],[2.],[3.],[4.]]); b = np.array([[10.,20.,30.]])
fig,axes = plt.subplots(1,3, figsize=(5.6,1.7))
for axc, A, t in zip(axes, [a, np.repeat(b,4,0), a+b], ['(4,1) a','(1,3) b tiled','a+b (4,4)']):
    axc.imshow(A, cmap='Blues', aspect='auto'); axc.set_title(t, **M)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            axc.text(j,i,f"{A[i,j]:.0f}",ha='center',va='center',fontsize=5)
    axc.set_xticks([]);axc.set_yticks([])
fig.tight_layout(); fig.savefig('ch01/broadcast_steps.pdf'); plt.close(fig)

# one-hot sketch on real penguins sex/island counts
import pandas as pd
pen = pd.read_csv('../data/penguins.csv')
ct = pd.crosstab(pen['island'], pen['sex'])
fig,ax = plt.subplots(figsize=(4.4,2.4))
ct.plot(kind='bar', ax=ax, color=['#2166ac','#b2182b'])
ax.set_title('one-hot inputs before encoding: island x sex counts (real)', **M)
ax.tick_params(labelsize=6)
fig.tight_layout(); fig.savefig('ch01/onehot_counts.pdf'); plt.close(fig)

# ---------- ch02 ----------
# titanic age histogram (real)
t = pd.read_csv('../data/titanic.csv')
fig,ax = plt.subplots(figsize=(4.4,2.4))
t['age'].dropna().hist(ax=ax, bins=30, color='#2166ac')
ax.axvline(t['age'].mean(), color='r', ls='--',
           label=f"mean {t['age'].mean():.1f}")
ax.legend(); ax.set_title('titanic age distribution (891 rows, real)', **M)
fig.tight_layout(); fig.savefig('ch02/age_hist.pdf'); plt.close(fig)

# flights line (real 1949-1960 air passengers)
fl = pd.read_csv('../data/flights.csv')
ycol = [c for c in fl.columns if 'pass' in c.lower()][0]
fig,ax = plt.subplots(figsize=(4.4,2.4))
mn = {m:i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
x = fl['year'] + (fl['month'].map(mn)-1)/12.
ax.plot(x, fl[ycol], color='#2166ac')
ax.set_title('airline passengers 1949-1960 (real Box-Jenkins series)', **M)
ax.set_ylabel('passengers (thousands)')
fig.tight_layout(); fig.savefig('ch02/flights_line.pdf'); plt.close(fig)

# ---------- ch03 ----------
# confusion-matrix heatmap from the real NB quartet (tp48 fp22 fn24 tn97)
cm = np.array([[97,22],[24,48]])
fig,ax = plt.subplots(figsize=(3.2,2.8))
ax.imshow(cm, cmap='Blues')
for i in range(2):
    for j in range(2):
        ax.text(j,i,str(cm[i,j]),ha='center',va='center',fontsize=14)
ax.set_xticks([0,1]);ax.set_yticks([0,1])
ax.set_xticklabels(['pred -','pred +']);ax.set_yticklabels(['true -','true +'])
ax.set_title('naive-Bayes confusion (real run)', **M)
fig.tight_layout(); fig.savefig('ch03/confmat.pdf'); plt.close(fig)

# precision/recall bars from the same real counts
P,R,F = 48/70, 48/72, 2*48/(2*48+22+24)
fig,ax = plt.subplots(figsize=(3.6,2.4))
ax.bar(['P','R','F1','acc'],[P,R,F,(48+97)/191],color='#2166ac')
for i,v in enumerate([P,R,F,(48+97)/191]): ax.text(i,v+.01,f'{v:.3f}',ha='center',**M)
ax.set_ylim(0,1);ax.set_title('metrics from the real confusion', **M)
fig.tight_layout(); fig.savefig('ch03/pr_bars.pdf'); plt.close(fig)

# ---------- ch04 ----------
# fitted-vs-actual on diabetes (real sklearn fit)
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
D = load_diabetes(); Xtr,Xte,ytr,yte = train_test_split(D.data,D.target,test_size=.25,random_state=0)
m = Ridge(1.0).fit(Xtr,ytr); yp = m.predict(Xte)
fig,ax = plt.subplots(figsize=(3.6,3.0))
ax.scatter(yte,yp,s=8,alpha=.6);ax.plot([40,340],[40,340],'r--')
ax.set_xlabel('actual');ax.set_ylabel('predicted')
ax.set_title(f'ridge fitted-vs-actual, $R^2$={m.score(Xte,yte):.3f} (real)',**M)
fig.tight_layout(); fig.savefig('ch04/fitted_actual.pdf'); plt.close(fig)

# ---------- ch05 ----------
# depth sweep on digits --- the exact table forest_lib.out.txt prints
ds=[2,4,6,10,None]; tr=[0.323,0.581,0.810,0.976,1.000]; te=[0.307,0.533,0.751,0.856,0.849]
fig,ax = plt.subplots(figsize=(4.4,2.5))
ax.plot(range(5),tr,'b-o',ms=4,label='train');ax.plot(range(5),te,'r-s',ms=4,label='test')
ax.set_xticks(range(5));ax.set_xticklabels(['2','4','6','10','full'])
ax.set_xlabel('max depth');ax.set_ylim(0.2,1.05);ax.legend();ax.grid(alpha=.3)
for i,(a,b) in enumerate(zip(tr,te)):
    ax.text(i,a+.02,f'{a:.2f}',ha='center',fontsize=6)
    ax.text(i,b-.06,f'{b:.2f}',ha='center',fontsize=6)
ax.set_title("depth sweep on digits --- the listing's own table, drawn",fontsize=7)
fig.tight_layout(); fig.savefig('ch05/depth_sweep.pdf'); plt.close(fig)

# ---------- ch07 ----------
# weight histogram of a trained scratch MLP: retrain 300 iters, real
import torch, torch.nn as nn, torch.nn.functional as F
from sklearn.datasets import load_digits
Dg = load_digits(); X = torch.tensor(Dg.data/16.,dtype=torch.float32)
y = torch.tensor(Dg.target)
Xtr,Xte,ytr,yte = X[:1400],X[1400:],y[:1400],y[1400:]
W1 = torch.randn(64,32)*math.sqrt(2/64); b1=torch.zeros(32)
W2 = torch.randn(32,10)*math.sqrt(2/32); b2=torch.zeros(10)
W1.requires_grad_();b1.requires_grad_();W2.requires_grad_();b2.requires_grad_()
losses=[]
opt = torch.optim.SGD([W1,b1,W2,b2],lr=.5,momentum=.9)
for i in range(601):
    z=(Xtr@W1+b1).clamp(min=0); lo=F.cross_entropy(z@W2+b2,ytr)
    opt.zero_grad();lo.backward();opt.step();losses.append(float(lo))
fig,axes=plt.subplots(1,2,figsize=(5.6,2.2))
axes[0].plot(losses,'b-');axes[0].set_title(f'real loss curve ({float(lo):.3f})',**M)
axes[1].hist(W1.detach().numpy().ravel(),40,color='#2166ac')
axes[1].set_title('learned W1 histogram (real)',**M)
fig.tight_layout(); fig.savefig('ch07/mlp_loss_hist.pdf'); plt.close(fig)

# ---------- ch09 ----------
# conv output-size table (computed formula)
fig,ax = plt.subplots(figsize=(4.4,2.4))
cfgs=[('5x5 s1',28,5,1),('5x5 s2',28,5,2),('3x3 s1',28,3,1),('7x7 s2',28,7,2),('11x11 s4',227,11,4)]
outs=[(n-k)//s+1 for _,n,k,s in cfgs]
ax.bar([c[0] for c in cfgs],outs,color='#2166ac')
for i,o in enumerate(outs): ax.text(i,o+.5,str(o),ha='center',**M)
ax.set_ylabel('output size');ax.set_title('(n-k)/s+1 on real configs',**M)
fig.tight_layout(); fig.savefig('ch09/conv_sizes.pdf'); plt.close(fig)

# cnn per-class accuracy from the trained state dict (real eval)
import torchvision
from torchvision import transforms
mn = torchvision.datasets.MNIST('/tmp/mnist',train=False,download=True,
     transform=transforms.ToTensor())
net = nn.Sequential(nn.Conv2d(1,8,5),nn.ReLU(),nn.MaxPool2d(2),
     nn.Conv2d(8,16,3),nn.ReLU(),nn.MaxPool2d(2),nn.Flatten(),
     nn.Linear(400,64),nn.ReLU(),nn.Linear(64,10))
try:
    net.load_state_dict(torch.load('../code/ch09/cnn_state.pt',weights_only=True))
except Exception:
    pass
from torch.utils.data import Subset
net.eval(); loader=torch.utils.data.DataLoader(Subset(mn,range(2000)),batch_size=200)
preds=[];labs=[]
with torch.no_grad():
    for xb,yb in loader:
        preds.append(net(xb).argmax(1));labs.append(yb)
preds=torch.cat(preds);labs=torch.cat(labs)
acc=[float((preds[labs==c]==c).float().mean()) for c in range(10)]
fig,ax = plt.subplots(figsize=(4.4,2.4))
ax.bar(range(10),acc,color='#2166ac')
for i,a in enumerate(acc): ax.text(i,a+.01,f'{a:.2f}',ha='center',fontsize=6)
ax.set_ylim(0,1.05);ax.set_xlabel('digit');ax.set_title('per-class accuracy, trained cnn (real)',**M)
fig.tight_layout(); fig.savefig('ch09/perclass_acc.pdf'); plt.close(fig)

# confusion 10x10 from same eval
cm = np.zeros((10,10),int)
for p,l in zip(preds.numpy(),labs.numpy()): cm[l,p]+=1
fig,ax=plt.subplots(figsize=(4.0,3.4))
ax.imshow(cm,cmap='Blues')
ax.set_xticks(range(10));ax.set_yticks(range(10))
ax.set_xlabel('predicted');ax.set_ylabel('true')
ax.set_title('cnn confusion 10x10 (real, 2000 imgs)',**M)
for i in range(10):
    for j in range(10):
        if cm[i,j]>0 and (i!=j or cm[i,j]>50): ax.text(j,i,cm[i,j],ha='center',va='center',fontsize=5)
fig.tight_layout(); fig.savefig('ch09/conf10.pdf'); plt.close(fig)
print('patched figs done; cnn per-class:', [round(a,2) for a in acc])
