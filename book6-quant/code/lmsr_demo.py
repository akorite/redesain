import numpy as np
# LMSR: cost C = b*log(sum exp(q_i/b)); price of YES = exp(q_Y/b)/(exp(q_Y)+exp(q_N))
b = 100.0
def price(qy,qn): return np.exp(qy/b)/(np.exp(qy/b)+np.exp(qn/b))
def cost(qy,qn): return b*np.log(np.exp(qy/b)+np.exp(qn/b))
qy=qn=0.0
print(f"b={b:.0f}: start price {price(qy,qn):.3f}")
c0=cost(qy,qn)
# buy 50 YES: cost = C(qy+50)-C(qy)
qy+=50; c1=cost(qy,qn)
print(f"buy 50 YES: paid {c1-c0:.2f}  avg px {(c1-c0)/50:.3f}  new YES px {price(qy,qn):.3f}")
# buy another 50 at the worse price
c2=cost(qy,qn); qy+=50; c3=cost(qy,qn)
print(f"buy 50 more: paid {c3-c2:.2f}  avg px {(c3-c2)/50:.3f}  new YES px {price(qy,qn):.3f}")
# subsidy property: max loss = b*ln2
print(f"market-maker worst case = b*ln2 = {b*np.log(2):.1f}")
# compare to orderbook: same trade on a 0.5-spread book at depth d needs liquidity
print("vs orderbook: LMSR always quotes (depth=b), book depth vanishes when you need it")
