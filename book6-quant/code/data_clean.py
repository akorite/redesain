"""Clean raw trade prints: dedupe, ordering, bad-tick screen."""
import csv, time
tr=[]
with open("data/btc_trades.csv") as fh:
    reader=csv.reader(fh); next(reader,None)
    for row in reader:
        tr.append((float(row[2]), float(row[0]), float(row[1])))  # t, price, vol
n0=len(tr)
# dedupe exact (t,price,vol)
seen=set(); tr2=[]
for x in tr:
    if x not in seen: seen.add(x); tr2.append(x)
# enforce nondecreasing time
tr2.sort()
# bad ticks: |return| > 8x rolling sd of neighbours
import numpy as np
px=np.array([x[1] for x in tr2]); r=np.diff(px)/px[:-1]
sd=r.std(); bad=np.where(np.abs(r)>8*sd)[0]
print(f"raw {n0} prints -> dedup {len(tr2)}  (dupes {n0-len(tr2)})")
print(f"price span {px.min()} .. {px.max()}")
print(f"return sd {sd*1e4:.2f}bp; |r|>8sd ticks: {len(bad)}")
gaps=np.diff([x[0] for x in tr2])
print(f"max time gap between prints {gaps.max():.0f}s  mean {gaps.mean():.1f}s")
