import pandas as pd, numpy as np
d = pd.read_csv("data/btc_daily.csv")
r = np.log(d["c"]).diff().dropna().to_numpy()
n = len(r)
# rolling 250-day historical 95% VaR, then count exceedances in next 250
W=250
var = np.full(n, np.nan)
for i in range(W,n):
    var[i] = np.percentile(r[i-W:i], 5)
bt = r[W:]
vr = var[W:]
exc = bt < vr
print(f"95% VaR backtest, {len(bt)} days after {W}-day warmup")
print(f"expected exceedances: {0.05*len(bt):.1f}   observed: {exc.sum()}")
print(f"exceedance rate: {exc.mean()*100:.1f}% (target 5%)")
# clustering: max gap between exceedances and consecutive pairs
idx = np.where(exc)[0]
cons = np.sum(np.diff(idx)==1)
print(f"consecutive-day exceedance pairs: {cons} (clustering of bad days)")
print(f"worst breach: {bt.min()*100:.1f}% vs its VaR {vr[np.argmin(bt)]*100:.1f}%")
