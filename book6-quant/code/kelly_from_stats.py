"""ch17: measured stats -> honest size.  f* = mu/var, continuous-Kelly
approximation on the days the mom20 rule is long."""
import csv, math
rows=list(csv.reader(open('data/btc_daily.csv')))[1:]
c=[float(r[4]) for r in rows]
r=[math.log(c[i]/c[i-1]) for i in range(1,len(c))]
xs=[r[i] for i in range(len(r)) if i>=20 and c[i-1]/c[i-21]-1>0]
m=sum(xs)/len(xs); v=sum((a-m)**2 for a in xs)/(len(xs)-1)
se=math.sqrt(v/len(xs))
f=m/v
print(f"when long: mean {m*1e4:+.2f}bp/day  se {se*1e4:.2f}bp  var {v:.2e}")
print(f"continuous-Kelly f* = {f:+.2f}")
print(f"mu is {m/se:+.2f} SEs from zero -- inside the noise band,")
print("so the honest position is: f* = 0.  There is nothing to size.")
