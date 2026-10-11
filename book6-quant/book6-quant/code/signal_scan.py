"""ch17: candidate momentum signals on the CORRECTED pinned tape.
Convention: position on day i uses signal c[i-1]/c[i-1-L]-1 > 0."""
import csv, math, sys
path = sys.argv[1] if len(sys.argv)>1 else 'data/btc_daily.csv'
rows=list(csv.reader(open(path)))[1:]
c=[float(r[4]) for r in rows]
r=[math.log(c[i]/c[i-1]) for i in range(1,len(c))]
def sharpe(x):
    m=sum(x)/len(x); v=sum((a-m)**2 for a in x)/(len(x)-1)
    return m/math.sqrt(v)*math.sqrt(365) if v>0 else 0
print(f"file: {path.split('/')[-1]}")
for L,name in ((1,'mom1'),(20,'mom20')):
    ys=[r[i] for i in range(len(r)) if i>=L and c[i-1]/c[i-1-L]-1>0]
    edge=(sum(ys)/len(ys))*1e4 if ys else 0
    print(f"{name}: n={len(ys)}  mean_when_long={edge:+.2f}bp/day  ann_sharpe={sharpe(ys):+.2f}")
print("honest verdict: tiny edge, not the number the other file promised")
