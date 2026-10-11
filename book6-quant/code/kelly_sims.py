import numpy as np
rng=np.random.default_rng(13)
p=0.55; b=1.0
fs=np.linspace(0,1,41)
G=np.empty(len(fs))
for i,f in enumerate(fs):
    # growth rate per toss: p log(1+f b)+(1-p)log(1-f)
    G[i]=p*np.log(1+f*b)+(1-p)*np.log(1-f) if f<1 else -np.inf
fb=fs[np.argmax(G)]
print(f"coin p={p} b={b}:  f* = {fb:.2f}   (theory {p-(1-p):.2f})")
print(f"growth at f* {G[np.argmax(G)]:+.4f}/toss   at 2f* {G[np.argmin(np.abs(fs-2*fb))]:+.4f}   at 3f* {G[np.argmin(np.abs(fs-3*fb))]:+.4f}")
# sim: full vs half vs double kelly paths
for f in (fb, fb/2, 2*fb):
    w=np.cumprod(1+f*np.where(rng.random(2000)<p, b, -1.0))
    print(f"f={f:.2f}: final {w[-1]:9.1f}   median path dd {((np.maximum.accumulate(w)-w)/np.maximum.accumulate(w)).max():.1%}")
with open("/tmp/KG.tex","w") as fh:
    for i,f in enumerate(fs): fh.write(f"{f:.3f} {G[i]:+.4f}\n")
