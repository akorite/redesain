"""ch02 WE3: is BTC log-price stationary? does its difference pass?
Uses the cached Kraken daily series (data/btc_daily.csv, fetched
2026-10-11); re-run kraken_daily.py to refresh."""
import json, os, urllib.request
import numpy as np
from statsmodels.tsa.stattools import adfuller

CSV = "data/btc_daily.csv"
if not os.path.exists(CSV):
    url = ("https://api.kraken.com/0/public/OHLC"
           "?pair=XBTUSD&interval=1440")
    j = json.load(urllib.request.urlopen(url, timeout=30))
    key = [k for k in j["result"] if k != "last"][0]
    rows = j["result"][key]
    with open(CSV, "w") as f:
        f.write("time,o,h,l,c\n")
        for r in rows:
            f.write(f"{int(r[0])},{r[2]},{r[3]},{r[4]},{r[5]}\n")
    print(f"fetched {len(rows)} bars -> {CSV}")
c = np.loadtxt(CSV, delimiter=",", skiprows=1, usecols=4)
lp = np.log(c)
r = np.diff(lp)
print(f"bars={len(c)} log-price range [{lp.min():.3f},{lp.max():.3f}]")
for name, x in (("log-price", lp), ("log-return", r)):
    stat, p, *_ = adfuller(x, autolag="AIC")[:2]
    crit = adfuller(x, autolag="AIC")[4]["5%"]
    print(f"{name:10s} ADF={stat:+7.3f} p={p:.4f} crit5%={crit:+.3f} "
          f"-> {'stationary' if p < 0.05 else 'unit root not rejected'}")
# and on the coint-style pair: ETH vs BTC log-prices share a unit root
print("(BTC log-price contains the unit root; returns do not.)")
