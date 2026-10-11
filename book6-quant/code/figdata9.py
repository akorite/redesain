import numpy as np
rng=np.random.default_rng(7)
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
n_strat,n_days=300,500
ts=np.empty(n_strat)
for k in range(n_strat): ts[k]=sharpe(rng.normal(0,1,n_days))
with open("/tmp/S_HIST.tex","w") as fh:
    h,e=np.histogram(ts,20)
    for i in range(20): fh.write(f"{(e[i]+e[i+1])/2:.3f} {h[i]}\n")
grid=[]
for a in range(2,60):
    for b in range(a+5,200,5):
        grid.append((a,b))
with open("/tmp/GRID.tex","w") as fh:
    for i,(a,b) in enumerate(grid):
        # synthetic: sharpe decays with distance from best, plus noise
        s=0.6-0.004*((a-46)**2+(b-56)**2)**0.5+rng.normal(0,0.15)
        fh.write(f"{a} {b} {s:.3f}\n")
with open("/tmp/BESTN.tex","w") as fh:
    for N in [1,3,10,30,100,300,1000]:
        fh.write(f"{N} {np.sqrt(2*np.log(N)):.3f}\n")
print("ok")
