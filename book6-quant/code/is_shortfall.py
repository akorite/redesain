import numpy as np
rng=np.random.default_rng(2)
Q=1e5; sig=0.02; V=1e6
def impact_bp(q): return sig*np.sqrt(q/V)*1e4
print(f"instant IS: {impact_bp(Q):+.1f}bp")
i=impact_bp(Q/2)
drift=rng.normal(0,0.004)*1e4
print(f"split  IS: {i:+.1f}bp impact + {drift:+.1f}bp drift on half = {i+drift/2:+.1f}bp")
print("splitting trades speed for risk: less impact, more timing exposure")
