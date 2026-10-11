import pandas as pd, numpy as np
t = pd.read_csv("data/btc_trades.csv")
gaps = np.diff(t["time"])
print(f"inter-print gaps: n={len(gaps)}  median {np.median(gaps)*1000:.0f}ms")
print(f"p95 {np.percentile(gaps,95)*1000:.0f}ms  max {gaps.max():.1f}s")
big = gaps > np.median(gaps)*20
print(f"gaps >20x median: {big.sum()} ({big.sum()/len(gaps)*100:.1f}%)")
# burstiness: prints per 10s window
w = (t["time"]-t["time"].min())/10
cnt = pd.Series(1,index=w.astype(int)).groupby(level=0).sum()
print(f"prints/10s: mean {cnt.mean():.1f}  max {cnt.max()}  zeros {10-len(cnt) if len(cnt)<10 else 0}")
print("arrival process is clustered -- Poisson would show smoother counts")
