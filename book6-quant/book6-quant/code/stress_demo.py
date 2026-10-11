import csv, math
r=[]
with open("data/btc_daily.csv") as fh:
    rd=csv.reader(fh); next(rd)
    px=[float(row[4]) for row in rd]
r=[math.log(px[i]/px[i-1]) for i in range(1,len(px))]
rs=sorted(r)
print("named-day stress on a flat long book:")
for name,p in [("5% day",0.05),("1% day",0.01),("worst day",0)]:
    x=rs[int(p*len(rs))] if p>0 else rs[0]
    print(f"  {name}: {x*100:+.2f}% on the book (x leverage)")
print("vol-regime stress: last-90d vol vs full-sample")
import statistics as st
print(f"  full {st.stdev(r)*math.sqrt(365)*100:.0f}% ann.   last-90 {st.stdev(r[-90:])*math.sqrt(365)*100:.0f}% ann.")
