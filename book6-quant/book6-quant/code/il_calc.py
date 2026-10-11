"""Impermanent loss vs holding, as a function of price ratio r."""
import numpy as np
def il(r): return 2*np.sqrt(r)/(1+r)-1
for r in (0.25,0.5,0.8,1.0,1.25,1.5,2.0,4.0):
    print(f"r={r:4.2f}: IL={il(r)*100:+6.2f}%")
# break-even fee: volume*fraction*fee vs IL
print("breakeven: daily volume v (in pool units), fee 0.3% -> v*0.003 > -IL")
r=1.5; need=-il(r)/0.003
print(f"r=1.5 needs daily turnover > {need:.2f}x pool TVL to break even (30d: {need/30:.3f}x)")
