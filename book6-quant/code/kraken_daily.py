"""kraken_daily.py -- WE3: real BTC daily bars from Kraken's public OHLC.

No API key. Endpoint verified live 2026-10-11 (HTTP 200); see
docs/unverified.md for the standing re-check note. Kraken returns
rows [time, open, high, low, close, vwap, volume, count].
"""
import json
import urllib.request

import numpy as np
import pandas as pd

URL = ("https://api.kraken.com/0/public/OHLC"
       "?pair=XBTUSD&interval=1440&since=1704067200")  # 2024-01-01 UTC


def fetch(url=URL):
    with urllib.request.urlopen(url, timeout=30) as f:
        j = json.load(f)
    assert not j["error"], j["error"]
    key = next(k for k in j["result"] if k != "last")
    rows = j["result"][key]
    df = pd.DataFrame(rows, columns=["time", "o", "h", "l", "c",
                                     "vwap", "vol", "count"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    for col in ["o", "h", "l", "c"]:
        df[col] = df[col].astype(float)
    return df[["time", "o", "h", "l", "c"]]


if __name__ == "__main__":
    df = fetch()
    df["r"] = np.log(df["c"] / df["c"].shift(1))
    rr = df["r"].dropna()
    print(df.head(3).to_string(index=False))
    print("...")
    print("bars:", len(df), "| returns:", len(rr))
    print(f"mean r = {rr.mean():+.5f}  sd = {rr.std(ddof=1):.5f}"
          f"  ann sd = {rr.std(ddof=1)*np.sqrt(365):.3f}")
    print(f"skew   = {rr.skew():+.3f}   excess kurtosis = "
          f"{rr.kurtosis():+.3f}  (normal = 0)")
    # QQ evidence: fraction beyond 3 sds vs the 0.27% normal guess
    z = (rr - rr.mean()) / rr.std()
    print(f"|z|>3: {(z.abs() > 3).mean():.4f}  (normal ~ 0.0027)")
    q = np.quantile(z, [0.01, 0.5, 0.99])
    print("sample 1%/50%/99% quantiles of z:", np.round(q, 3))
