"""Perp premium -> funding payments; PnL decomposition. seed fixed."""
import numpy as np
rng=np.random.default_rng(7)
T=720  # 30 days of hourly funding
index=50000*np.exp(np.cumsum(rng.normal(0,0.004,T)))
# premium: mean-reverting around 0 with noise (basis in bps/hour)
prem=np.zeros(T); 
for t in range(1,T): prem[t]=0.7*prem[t-1]+0.04+rng.normal(0,3)
# funding rule: rate = premium index (8h MA), clamp +-0.05%/h  [simplified venue rule]
f=np.convolve(prem,np.ones(8)/8,'same'); f=np.clip(f,-5,5)/1e4
pos=+1; notl=2.0  # long 2 BTC
pay=pos*notl*f*index  # paid each hour by longs when f>0
idx=index[-1]; 
print(f"T={T}h  mean funding {f.mean()*1e4:.3f}bp/h  sum {f.sum()*1e4:.2f}bp  ~APR {f.sum()*1e4*365/30:.0f}bp")
print(f"long pays {pay.sum():+,.0f} USD over 30d (positive = paid by longs)")
pnl=pos*notl*(idx-index[0])-pay.sum()
print(f"price PnL {pos*notl*(idx-index[0]):+,.0f}  funding {-pay.sum():+,.0f}  net {pnl:+,.0f}")
# carry: short perp + long spot = earn funding, zero delta
carry=pay.sum()/index[0]/notl
print(f"short-perp carry yield 30d: {carry*1e4:.1f}bp of notional")
