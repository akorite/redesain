import numpy as np
rng=np.random.default_rng(4)
n=1200; r=np.empty(n)
r[:400]=rng.normal(0.001,0.01,400); r[400:800]=rng.normal(0,0.005,400); r[800:]=rng.normal(-0.0005,0.02,400)
with open("/tmp/REG.tex","w") as fh:
    for i in range(0,n,10): fh.write(f"{i} {np.cumsum(r)[i]:.3f}\n")
# fold IS vs OOS from wf_demo
pts=[(2.35,1.86),(2.11,0.55),(1.51,-0.52),(1.16,1.15)]
with open("/tmp/FOLDS.tex","w") as fh:
    for a,b in pts: fh.write(f"{a:.2f} {b:.2f}\n")
print("ok")
