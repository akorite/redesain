import numpy as np
# pool: x token, y quote. spot = y/x
x0, y0 = 1000.0, 50000.0   # spot 50
k = x0*y0
m_ext = 55.0               # external venue price
print(f"pool spot {y0/x0}, external {m_ext} -> pool cheap, arb buys token here")
# buy dx paying dy: new price = m_ext -> y1/x1 = m_ext with x1*y1=k
x1 = np.sqrt(k/m_ext); y1 = np.sqrt(k*m_ext)
dx = x0 - x1; dy = y1 - y0
print(f"buy {dx:.4f} token for {dy:.2f} quote")
print(f"pool pays avg {dy/dx:.4f} vs external {m_ext} -> sell token outside")
profit = dx*m_ext - dy
print(f"arb revenue {dx*m_ext:.2f} cost {dy:.2f} profit {profit:.2f}")
print(f"new spot {y1/x1:.4f} (restored to external)")
f = 0.003
dy_fee = (y1-y0)/(1-f)
print(f"with 0.3% fee: cost {dy_fee:.2f} profit {dx*m_ext-dy_fee:.2f} (fee shaves {dy_fee-dy:.2f})")
