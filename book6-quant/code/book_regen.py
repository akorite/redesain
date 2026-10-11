import pandas as pd, numpy as np
t = pd.read_csv("data/btc_trades.csv")
t["ts"] = pd.to_datetime(t["time"],unit="s")
t = t.sort_values("ts")
# reconstruct mid from print stream: last trade price ~ mid proxy
p = t["price"].to_numpy()
s = np.where(t["side"]=="b",1,-1)
v = t["vol"].to_numpy()
# order-flow imbalance (OFI) in rolling 100-print windows
w=100
ofi = pd.Series(s*v).rolling(w).sum()
vol_sh = pd.Series(v).rolling(w).sum()
dp = pd.Series(p).diff().shift(-1)
print(f"OFI vs next-print move over {len(p)} prints")
sub = slice(w, len(p)-10)
corr = np.corrcoef(ofi[sub]/vol_sh[sub], dp[sub])[0,1]
print(f"corr(OFI, dp_next) = {corr:+.3f}")
print(f"mean |dp| when |OFI/vol|>0.5: {dp[sub][np.abs(ofi[sub]/vol_sh[sub])>0.5].abs().mean():.4f}")
print(f"mean |dp| when |OFI/vol|<0.1: {dp[sub][np.abs(ofi[sub]/vol_sh[sub])<0.1].abs().mean():.4f}")
