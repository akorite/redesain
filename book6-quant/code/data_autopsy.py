"""ch17: forensics on a pinned dataset -- prove the columns are what
the header claims BEFORE trusting any statistic downstream.
Compares the scrambled snapshot vs the corrected file."""
import csv, math

def cols(path):
    rows=list(csv.reader(open(path))); hdr=rows[0]
    t=[list(map(float,r)) for r in rows[1:]]
    return hdr, [c[0] for c in t], [[c[i] for c in t] for i in range(1,5)]

for path in ("data/btc_daily_scrambled.csv","data/btc_daily.csv"):
    hdr,t,C = cols(path)
    o,h,l,c = C
    # A real open must equal yesterday's close in continuous daily bars.
    gap = max(abs(o[i]-c[i-1]) for i in range(1,len(t)))
    # A real high must be >= open and close; real low <= open and close.
    hv  = sum(1 for i in range(len(t)) if h[i] < o[i]-1e-6 or h[i] < c[i]-1e-6)
    lv  = sum(1 for i in range(len(t)) if l[i] > o[i]+1e-6 or l[i] > c[i]+1e-6)
    # VWAP signature: always inside [l,h] AND between min(o,c),max(o,c)? no --
    # instead test monotonic relation: vwap == vwap iff l<=v<=h always.
    print(f"{path.split('/')[-1]}: header={hdr}")
    print(f"  max |open_t - close_{{t-1}}| = {gap:12.2f}  (real daily bars: ~0)")
    print(f"  'high' col violations h>=o,h>=c: {hv}")
    print(f"  'low'  col violations l<=o,l<=c: {lv}")
    print(f"  col2>=all? {all(h[i]>=max(o[i],c[i])-1e-6 for i in range(len(t)))}")
