import pandas as pd, numpy as np
t = pd.read_csv("data/btc_trades.csv")
p = t["price"].to_numpy()
r = np.diff(np.log(p))
print(f"print-to-print moves: n={len(r)}  std={r.std()*1e4:.2f}bp  max={np.abs(r).max()*1e4:.2f}bp")
for s in [2,3,5,10]:
    fl = np.abs(r) > s*r.std()
    print(f"|dp|>{s}sigma: {fl.sum()} prints flagged")
print(f"largest move = {np.abs(r).max()/r.std():.1f} sigma but only {np.abs(r).max()*1e4:.2f}bp -- not a bad tick")
