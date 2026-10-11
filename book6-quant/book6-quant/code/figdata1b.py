import pandas as pd, numpy as np
d = pd.read_csv("data/btc_daily.csv")
r = np.log(d["c"]).diff().dropna().to_numpy()
with open("../figures/data/ACFMAG.tex","w") as f:
    for k in range(1,16):
        a = np.corrcoef(r[:-k], r[k:])[0,1]
        b = np.corrcoef(np.abs(r[:-k]), np.abs(r[k:]))[0,1]
        f.write(f"{k} {a:.4f} {b:.4f}\n")
print("wrote ACFMAG")
