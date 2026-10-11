import json
import numpy as np
# reliability curve (same sim as calibration.py)
rng=np.random.default_rng(3); n=4000
fore=np.clip(rng.normal(0.5,0.22,n),0.02,0.98)
actual=0.5+(fore-0.5)*0.55; y=rng.random(n)<actual
edges=np.linspace(0,1,11); idx=np.digitize(fore,edges)-1
with open("/tmp/R_REL.tex","w") as fh:
    for b in range(10):
        m=idx==b
        if m.sum()>30: fh.write(f"{fore[m].mean():.4f} {y[m].mean():.4f}\n")
# E[Brier](p) curve, q=0.6
q=0.6
with open("/tmp/S_BRIER.tex","w") as fh:
    for p in np.linspace(0.02,0.98,60):
        fh.write(f"{p:.3f} {q*(p-1)**2+(1-q)*p**2:.4f}\n")
# resolution path
r=np.random.default_rng(1); T=200; W=r.random(T)<0.6
px=np.convolve(W.astype(float),np.ones(10)/10,'same')
with open("/tmp/P_PATH.tex","w") as fh:
    for t in range(0,T,4): fh.write(f"{t} {px[t]:.4f}\n")
# Polymarket YES-price histogram from real snapshot
d=json.load(open("data/pm_markets.json"))
ps=[]
for m in d:
    try: ps.append(float(json.loads(m["outcomePrices"])[0]))
    except: pass
hist,ed=np.histogram(ps,bins=np.linspace(0,1,21))
with open("/tmp/H_PM.tex","w") as fh:
    for i in range(20): fh.write(f"{ed[i]+0.025:.3f} {hist[i]}\n")
print(len(ps),"markets ->",hist.tolist())
