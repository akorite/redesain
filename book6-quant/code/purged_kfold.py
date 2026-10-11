import numpy as np
rng=np.random.default_rng(8)
n=600
shocks=rng.normal(0,0.01,n)
r=np.empty(n); r[0]=shocks[0]
for i in range(1,n): r[i]=0.3*r[i-1]+shocks[i]
px=np.cumprod(1+r)
feat=np.convolve(np.diff(np.log(px)),np.ones(10)/10,'valid')
W=30   # forward-label window
lab=np.empty(len(feat))
for i in range(len(feat)):
    lab[i]=px[min(i+W+1,n-1)]/px[min(i+2,n-1)]-1
K=5; fold=len(feat)//K
print(f"label window W={W}  adjacent-label corr {np.corrcoef(lab[:-1],lab[1:])[0,1]:.3f}")
tot=0
for k in range(1,K):
    b=k*fold
    overlap=sum(1 for i in range(len(feat)) if i<b and min(i+W+1,n-1)>=b+2)
    print(f"boundary {b}: {overlap} train labels reach into test fold")
    tot+=overlap
print(f"contiguous CV shares {tot} overlapping labels across {K-1} boundaries")
print("purge them + embargo W on each side, or the test is not a test")
