import pandas as pd, numpy as np
d = pd.read_csv("data/btc_daily.csv")
d["yr"] = pd.to_datetime(d["time"],unit="s").dt.year
r = np.log(d["c"]).diff()
d["r"] = r
print("per-year stats on real BTC daily (annualised x365):")
for yr,g in d.groupby("yr"):
    rr = g["r"].dropna()
    if len(rr)<10: continue
    s = rr.mean()/rr.std()*np.sqrt(365)
    mdd = ((1+rr).cumprod()/ (1+rr).cumprod().cummax() -1).min()
    print(f"{yr}: n={len(rr)}  sharpe {s:+.2f}  ret {((1+rr).prod()-1)*100:+6.1f}%  mdd {mdd*100:5.1f}%")
rr = d["r"].dropna()
s = rr.mean()/rr.std()*np.sqrt(365)
print(f"full window: sharpe {s:+.2f} -- the average of very different years")
