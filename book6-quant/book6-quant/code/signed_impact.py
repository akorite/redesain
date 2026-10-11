import pandas as pd, numpy as np
t = pd.read_csv("data/btc_trades.csv")
p = t["price"].to_numpy(); s = (t["side"]=="b").astype(float)*2-1
dp = np.diff(p)
print(f"prints {len(p)}: buys {(s>0).sum()} sells {(s<0).sum()}")
print(f"zero-move prints: {(dp==0).mean()*100:.0f}% of consecutive moves are 0")
mb = dp[s[:-1]>0].mean(); ms = dp[s[:-1]<0].mean()
print(f"avg next-print dp after a buy  = {mb:+.4f}")
print(f"avg next-print dp after a sell = {ms:+.4f}")
print(f"signed impact (spread/2 proxy) = {(mb-ms)/2:.4f} per print")
# per-print move in ticks (tick=0.1)
tick = 0.1
print(f"avg |dp| = {np.abs(dp).mean():.3f} = {np.abs(dp).mean()/tick:.2f} ticks")
