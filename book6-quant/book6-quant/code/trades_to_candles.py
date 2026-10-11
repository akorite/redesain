"""ch03 WE3: real trade prints -> resampled candles, checked against
the venue's own 1m OHLC. Kraken public endpoints, cached in data/."""
import json, os, time, urllib.request
import numpy as np

def get(path):
    return json.load(urllib.request.urlopen(
        "https://api.kraken.com/0/public/" + path, timeout=30))

TRADES = "data/btc_trades.csv"
if not os.path.exists(TRADES):
    key, rows, since = None, [], None
    for _ in range(6):                       # ~6000 prints
        q = "Trades?pair=XBTUSD" + (f"&since={since}" if since else "")
        j = get(q)
        key = [k for k in j["result"] if k != "last"][0]
        rows += j["result"][key]
        since = j["result"]["last"]
        time.sleep(0.4)
    rows.sort(key=lambda r: r[6])
    with open(TRADES, "w") as f:
        f.write("price,vol,time,side\n")
        for p, v, t, s, *_ in rows:
            f.write(f"{p},{v},{t},{s}\n")
    print(f"fetched {len(rows)} trades -> {TRADES}")

d = np.loadtxt(TRADES, delimiter=",", skiprows=1,
               converters={3: lambda s: 1.0 if s == b'"b"' else 0.0})
p, v, t, isbuy = d[:, 0], d[:, 1], d[:, 2], d[:, 3]
print(f"trades: {len(p)} span {t.min():.0f}..{t.max():.0f} "
      f"({(t.max()-t.min())/60:.1f} min) buy-share {isbuy.mean():.2f}")

# resample into 60s candles from the prints
t0 = int(t.min() // 60 * 60)
bins = {}
for pi, ti in zip(p, t):
    k = int((ti - t0) // 60)
    bins.setdefault(k, []).append(pi)
print("resampled candles (from prints):")
for k in sorted(bins):
    xs = bins[k]
    print(f"  t={t0+60*k} n={len(xs):3d} o={xs[0]:.1f} h={max(xs):.1f} "
          f"l={min(xs):.1f} c={xs[-1]:.1f}")

# venue 1m candles covering the same window
j = get(f"OHLC?pair=XBTUSD&interval=1&since={t0}")
key = [k for k in j["result"] if k != "last"][0]
v60 = {int(r[0] // 60 * 60): r for k2, r in
       ((int(r[0]) // 60, r) for r in j["result"][key])}
print("venue 1m candles (same window):")
for k in sorted(v60):
    r = v60[k]
    print(f"  t={k} o={r[1]} h={r[2]} l={r[3]} c={r[4]}")
