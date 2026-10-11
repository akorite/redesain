import numpy as np
rng = np.random.default_rng(2)
days=300; p=100.0; path=[p]
for d in range(days):
    p*= np.exp(rng.normal(0,0.02)); path.append(p)
print("same GBM path (sigma 2%/day, 300 days), three range widths:")
for w in [0.05,0.10,0.25]:
    inside = [abs(x/100-1)<w for x in path]
    inr = sum(inside)
    # CL multiplier ~ 1/(2*sqrt(w)) vs full-range for same liquidity
    mult = 1/(2*np.sqrt(w))
    print(f"range +/-{int(w*100):2d}%: in-range {inr}/300 ({inr/300*100:.0f}%)  "
          f"conc-mult {mult:.1f}x  fee-days-equiv {inr*mult:.0f}")
print("narrower width = fewer inside days x higher multiple")
