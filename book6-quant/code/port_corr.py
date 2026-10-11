import pandas as pd, numpy as np
t = pd.read_csv("data/btc_daily.csv")
r = np.log(t["c"]).diff().dropna().values
# rolling 60d correlation of btc returns to lagged momentum & vol regime
mom = pd.Series(t["c"]).pct_change(20).values[1:]
vol = pd.Series(r).rolling(60).std().values
# correlation of |r| clusters: autocorr of absolute returns at lags 1..10
ar = np.abs(r)
print("corr(|r_t|, |r_t-k|) -- vol clustering on real tape:")
for k in [1,2,5,10]:
    c = np.corrcoef(ar[k:], ar[:-k])[0,1]
    print(f"  lag {k}: {c:+.3f}")
# same for signed returns (should be ~0)
print("corr(r_t, r_t-k) -- signed:")
for k in [1,2,5,10]:
    c = np.corrcoef(r[k:], r[:-k])[0,1]
    print(f"  lag {k}: {c:+.3f}")
