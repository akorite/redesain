"""Basis = perp - spot; annualised; converge at funding epochs."""
import numpy as np
rng=np.random.default_rng(11)
T=720
spot=50000*np.exp(np.cumsum(rng.normal(0,0.004,T)))
basis=np.zeros(T)
for t in range(1,T):
    basis[t]=0.75*basis[t-1]+rng.normal(0,60)  # USD premium, mean-reverting
perp=spot+basis
ann=(perp[-1]/spot[-1]-1)*365/30
print(f"end: spot {spot[-1]:,.0f} perp {perp[-1]:,.0f} basis {basis[-1]:+.0f}")
print(f"basis = {(perp[-1]/spot[-1]-1)*1e4:+.1f}bp  annualised {ann*100:+.1f}%")
b_bp=(perp/spot-1)*1e4
print(f"basis stats: mean {b_bp.mean():+.1f}bp sd {b_bp.std():.1f}bp "
      f"|b|>20bp {np.mean(np.abs(b_bp)>20)*100:.1f}% of hours")
