import numpy as np
rng=np.random.default_rng(6)
r=np.concatenate([rng.normal(0.0008,0.004,1150), rng.normal(-0.03,0.01,10)])
np.random.default_rng(1).shuffle(r)
eq=np.cumsum(r)
with open("../figures/data/EQ12.tex","w") as fh:
    for i,e in enumerate(eq): fh.write(f"{i} {e:.4f}\n")
peak=np.maximum.accumulate(eq)
with open("../figures/data/DD12.tex","w") as fh:
    for i,e in enumerate(eq): fh.write(f"{i} {e-peak[i]:.4f}\n")
# skew demo histogram
r3=np.where(rng.random(500)<0.05, rng.normal(-0.08,0.02,500), rng.normal(0.007,0.002,500))
h,edges=np.histogram(r3,40)
with open("../figures/data/TAILH.tex","w") as fh:
    for i in range(40): fh.write(f"{(edges[i]+edges[i+1])/2:.4f} {h[i]}\n")
print("ok")
