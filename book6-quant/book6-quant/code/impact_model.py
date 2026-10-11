import numpy as np
# sqrt-law: cost per unit ~ sigma*sqrt(q/V)
sig=0.02; V=1e6
for q in [1e3,1e4,1e5,5e5]:
    c=sig*np.sqrt(q/V)
    print(f"q={q:>7.0f} ({q/V:.1%} of ADV)  impact {c*1e4:6.1f}bp")
