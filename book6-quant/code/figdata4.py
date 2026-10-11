import json
import numpy as np
# real funding series
d=json.load(open("data/hl_funding_btc.json"))
f=np.array([float(x["fundingRate"])*1e4 for x in d])
with open("../figures/data/F_FUND.tex","w") as fh:
    for i,v in enumerate(f): fh.write(f"{i} {v:.4f}\n")
# synthetic basis
rng=np.random.default_rng(11)
T=720; spot=50000*np.exp(np.cumsum(rng.normal(0,0.004,T)))
b=np.zeros(T)
for t in range(1,T): b[t]=0.75*b[t-1]+rng.normal(0,60)
bb=(b/spot)*1e4
with open("../figures/data/B_BASIS.tex","w") as fh:
    for t,v in enumerate(bb): fh.write(f"{t} {v:.2f}\n")
# leverage -> distance to liquidation, MM=0.5%
with open("../figures/data/L_LEV.tex","w") as fh:
    for lev in [1,2,3,5,7,10,15,20,25,30,40,50]:
        li=(1-(1/lev))/(1-0.005); fh.write(f"{lev} {(1-li)*100:.3f}\n")
print("fig data written", len(f), len(bb))
