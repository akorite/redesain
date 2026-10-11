"""ch03 figure coords: real-trade bid/ask bounce, depth->slippage."""
import numpy as np
from lob import Book

raw = [l.split(",") for l in
       open("data/btc_trades.csv").read().splitlines()[1:]]
p = np.array([float(r[0]) for r in raw])
isbuy = np.array([1.0 if r[3] == "b" else 0.0 for r in raw])
n = 160
p0 = p[:n]; isb = isbuy[:n]
p0 = p0 - p0.mean()
# approx mid: (last sell-print + last buy-print)/2
last_s, last_b, mid = None, None, []
for i in range(n):
    if isb[i] == 1: last_b = p0[i]
    else:           last_s = p0[i]
    mid.append(np.nan if last_s is None or last_b is None
               else (last_s + last_b) / 2)
def emit(name, pts):
    print(name, " ".join(f"({i},{v:.2f})" for i, v in pts if v == v))
emit("B_BUY",  [(i, p0[i]) for i in range(n) if isb[i] == 1])
emit("B_SELL", [(i, p0[i]) for i in range(n) if isb[i] == 0])
emit("B_MID",  [(i, mid[i]) for i in range(n)])

mid0 = None
out = []
for Q in (2, 3, 5, 6, 9, 12, 21, 36, 46):
    B2 = Book()
    for pr, q in [(99.0, 5), (99.5, 3), (100.0, 4)]: B2.add("b", pr, q)
    for pr, q in [(100.5, 2), (101.0, 3), (101.5, 6), (102.5, 10),
                  (104.0, 15), (106.0, 25)]: B2.add("s", pr, q)
    if mid0 is None: mid0 = B2.mid()
    n0 = len(B2.trades); B2.market("b", Q)
    fills = B2.trades[n0:]
    tot = sum(q for _, q, _ in fills)
    avg = sum(pp * qq for pp, qq, _ in fills) / tot
    out.append((Q, 100 * (avg / mid0 - 1)))
print("C_SLIP", " ".join(f"({q},{s:.3f})" for q, s in out))
