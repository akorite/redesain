import numpy as np
rng=np.random.default_rng(21)
p=0.55; b=1.0; T=2000
print(f"55/45 coin, {T} tosses, 200 seeds -- growth vs pain by fraction")
for f in [0.025,0.05,0.10,0.20,0.30,0.50]:
    g = p*np.log1p(f*b)+(1-p)*np.log1p(-f)
    finals=[]; dds=[]
    for s in range(200):
        w=np.cumprod(1+f*np.where(rng.random(T)<p,b,-1.0))
        finals.append(w[-1]); dds.append(1-w[-1]/np.maximum.accumulate(w)[-1] if False else (np.maximum.accumulate(w)-w).max()/np.maximum.accumulate(w).max())
    print(f"f={f:.3f}: G {g:+.4f}/toss  med final {np.median(finals):10.1f}  med dd {np.median(dds)*100:.0f}%  ruin<1: {(np.array(finals)<1).mean()*100:.0f}%")
