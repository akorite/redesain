"""Correct OHLCV resample: trades -> 5m bars, verify semantics."""
import csv, numpy as np
tr=[]
with open("data/btc_trades.csv") as fh:
    reader=csv.reader(fh); next(reader,None)
    for row in reader: tr.append((float(row[2]),float(row[0]),float(row[1])))
t0=int(tr[0][0]//300*300)
bars={}
for t,p,v in tr:
    b=int(t//300*300)
    if b not in bars: bars[b]=[p,p,p,p,0.0,0]
    o,h,l,c,vol,n=bars[b]
    bars[b]=[o,max(h,p),min(l,p),p,vol+v,n+1]
ks=sorted(bars)
print(f"{len(tr)} trades -> {len(ks)} 5m bars")
for b in ks[:3]:
    o,h,l,c,v,n=bars[b]
    print(f"t={b} o={o:.1f} h={h:.1f} l={l:.1f} c={c:.1f} v={v:.3f} n={n}")
# invariant check on one bar
b=ks[2]; o,h,l,c,v,n=bars[b]
ps=[p for t,p,vv in tr if int(t//300*300)==b]
assert abs(o-ps[0])<1e-9 and abs(c-ps[-1])<1e-9 and abs(h-max(ps))<1e-9 and abs(l-min(ps))<1e-9
print("bar semantics verified: o=first, h=max, l=min, c=last")
