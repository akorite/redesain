import pandas as pd, numpy as np
t = pd.read_csv("data/btc_trades.csv")
p = t["price"].to_numpy()
lr = np.diff(np.log(p))
qv = np.sum(lr**2)
net = np.log(p[-1]/p[0])
print(f"prints: {len(p)} over {(t.time.max()-t.time.min())/60:.1f} min")
print(f"quadratic variation = {qv:.2e}   (net return)^2 = {net**2:.2e}")
print(f"QV/net2 ratio = {qv/net**2:.2f} (<1: near-monotone directional walk)")
print(f"root-QV path move = {np.sqrt(qv)*100:.2f}% vs net {net*100:+.2f}%")
d = pd.read_csv("data/btc_daily.csv")
r = np.log(d["c"]).diff().dropna().to_numpy()
for k in [1,2,5,10,15]:
    a = np.corrcoef(r[:-k], r[k:])[0,1]
    b = np.corrcoef(np.abs(r[:-k]), np.abs(r[k:]))[0,1]
    print(f"k={k:2d}: acf(r)={a:+.3f}   acf(|r|)={b:+.3f}")
