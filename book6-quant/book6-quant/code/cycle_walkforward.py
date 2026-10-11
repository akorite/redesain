"""ch17: split-sample honesty on mom20 -- does the candidate survive OOS?
Same convention as signal_scan: c[i-1]/c[i-21]-1 > 0 earns r[i]."""
import csv, math
rows=list(csv.reader(open('data/btc_daily.csv')))[1:]
c=[float(r[4]) for r in rows]
r=[math.log(c[i]/c[i-1]) for i in range(1,len(c))]
xs=[r[i] for i in range(len(r)) if i>=20 and c[i-1]/c[i-21]-1>0]
def sharpe(x):
    m=sum(x)/len(x); v=sum((a-m)**2 for a in x)/(len(x)-1)
    return m/math.sqrt(v)*math.sqrt(365) if v>0 else 0
half=len(xs)//2
a,b=xs[:half],xs[half:]
eq=1.0
for x in xs: eq*=math.exp(x)
print(f"IS half : n={len(a)}  sharpe {sharpe(a):+.2f}  mean {sum(a)/len(a)*1e4:+.2f}bp")
print(f"OOS half: n={len(b)}  sharpe {sharpe(b):+.2f}  mean {sum(b)/len(b)*1e4:+.2f}bp")
print(f"full    : ret {100*(eq-1):+.1f}%  sharpe {sharpe(xs):+.2f}")
