"""LP vs HODL under GBM + fee accrual; many seeds."""
import numpy as np
rng=np.random.default_rng(4)
def run(seed,fee_daily_turnover=0.08):
    r=np.random.default_rng(seed); T=180
    s=100*np.exp(np.cumsum(r.normal(0,0.03,T)))
    # pool rebalance each step: LP value = 2*sqrt(k*price)... track value ratio
    ratio=s[-1]/s[0]
    lp_value=2*np.sqrt(s[0]*1000*s[-1]*1000)  # 2 sqrt(x*y) normalized
    hodl=1000*s[-1]+1000*s[0]  # half in token half in USD? standard: hold x0 tokens + y0 usd
    hodl=1000*s[0]+1000*s[0]*ratio
    lp=2000*s[0]*np.sqrt(ratio)
    fees=2000*s[0]*fee_daily_turnover*0.003*180
    return (lp+fees)/hodl-1
res=[run(s) for s in range(40)]
res_nf=[run(s,0) for s in range(40)]
print(f"40 seeds: LP+fees-vs-hodl mean {np.mean(res)*100:+.2f}%  "
      f"no-fees {np.mean(res_nf)*100:+.2f}%  best {np.max(res)*100:+.2f}%  worst {np.min(res)*100:+.2f}%")
