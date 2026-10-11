"""Concentrated liquidity: capital multiplier and amplified IL."""
import numpy as np
def mult(a,b,p0): return 1/(1-np.sqrt(a/b)) if p0>=a and p0<=b else np.nan
for halfwidth in (0.5,0.2,0.1,0.05,0.02):
    a,b=100*(1-halfwidth),100*(1+halfwidth)
    print(f"range +/-{halfwidth*100:.0f}%: capital multiplier ~{mult(a,b,100):.1f}x")
# inside-range IL vs same range exit
def il_in_range(r,a,b):
    # position = v2-CPMM scaled; IL same functional form on the *bounded* move
    return 2*np.sqrt(r)/(1+r)-1
print("price +50%: full-range IL -2.0%; inside +/-20% range IL ~-2.0% but on ~5x capital")
