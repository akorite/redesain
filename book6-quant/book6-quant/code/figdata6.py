import numpy as np
# IL curve
with open("../figures/data/I_IL.tex","w") as fh:
    for r in np.linspace(0.15,4.0,80):
        fh.write(f"{r:.3f} {100*(2*np.sqrt(r)/(1+r)-1):.3f}\n")
# price impact curve, x=1000,y=50000
with open("../figures/data/PI.tex","w") as fh:
    for dx in np.linspace(1,600,80):
        dxf=dx*0.997; out=dxf*50000/(1000+dxf); eff=out/dx
        fh.write(f"{dx:.1f} {100*(1-eff/50):.3f}\n")
# LP-vs-hodl path, one seed
r=np.random.default_rng(2); T=180
s=100*np.exp(np.cumsum(r.normal(0,0.03,T)))
with open("../figures/data/LP_PATH.tex","w") as fh:
    for t in range(T):
        ratio=s[t]/s[0]; lp=2000*s[0]*np.sqrt(ratio); hodl=1000*s[0]+1000*s[0]*ratio
        fh.write(f"{t} {100*(lp/hodl-1):.3f}\n")
print("done")
