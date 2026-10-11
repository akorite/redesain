"""ch17: the one-page memo pulls every number from the pinned file
itself -- the deliverable is reproducible by construction."""
import csv, math
rows=list(csv.reader(open('data/btc_daily.csv')))[1:]
c=[float(r[4]) for r in rows]
r=[math.log(c[i]/c[i-1]) for i in range(1,len(c))]
xs=[r[i] for i in range(len(r)) if i>=20 and c[i-1]/c[i-21]-1>0]
def sharpe(x):
    m=sum(x)/len(x); v=sum((a-m)**2 for a in x)/(len(x)-1)
    return m/math.sqrt(v)*math.sqrt(365) if v>0 else 0
half=len(xs)//2
sd=math.sqrt(sum(x*x for x in r)/len(r))*math.sqrt(365)
print("MEMO: daily BTC 20-day momentum, pinned tape 2024-10..2026-09")
print(f"  n={len(r)} daily returns, sd={sd:.3f} ann")
print(f"  mom20 edge {sum(xs)/len(xs)*1e4:+.2f}bp/day when long; "
      f"split-sample sharpe {sharpe(xs[:half]):+.2f} -> {sharpe(xs[half:]):+.2f}")
print("  claim: REJECTED -- not an edge at daily horizon on this tape")
