import csv, numpy as np
tr=[]
with open("data/btc_trades.csv") as fh:
    r=csv.reader(fh); next(r)
    for row in r: tr.append((float(row[2]),float(row[0])))
t0=tr[0][0]
with open("../figures/data/PRT.tex","w") as fh:
    for t,p in tr[::3]: fh.write(f"{t-t0:.0f} {p:.1f}\n")
# 1m closes for line
bars={}
for t,p in tr:
    b=int(t//60*60)
    bars.setdefault(b,[]).append(p)
with open("../figures/data/C1M.tex","w") as fh:
    for b in sorted(bars): fh.write(f"{b-t0:.0f} {bars[b][-1]:.1f}\n")
print(len(tr),"prints,",len(bars),"minutes")
