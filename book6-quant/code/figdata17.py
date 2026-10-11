"""ch17 figure data -> ../figures/data/. Equity curves for mom20 on
corrected vs scrambled tape, plus the autopsy violation counts."""
import csv, math, os
out='../figures/data'; os.makedirs(out, exist_ok=True)
def load(p):
    rows=list(csv.reader(open(p)))[1:]
    return [float(r[4]) for r in rows]
for tag,path in (('corr','data/btc_daily.csv'),('scram','data/btc_daily_scrambled.csv')):
    c=load(path); r=[math.log(c[i]/c[i-1]) for i in range(1,len(c))]
    eq_m,eq_b=1.0,1.0
    with open(f'{out}/ch17-equity-{tag}.dat','w') as f:
        for i in range(len(r)):
            if i>=20 and c[i-1]/c[i-21]-1>0: eq_m*=math.exp(r[i])
            eq_b*=math.exp(r[i])
            f.write(f"{i} {eq_m:.6f} {eq_b:.6f}\n")
with open(f'{out}/ch17-autopsy.dat','w') as f:
    f.write("name scram corr\n"
            "hgap 10115 62.9\n"
            "hviol 721 0\n"
            "lviol 384 0\n")
with open(f'{out}/ch17-signal.dat','w') as f:
    f.write("name scram corr\nmom1 -0.03 0.18\nmom20 0.70 0.26\n")
with open(f'{out}/ch17-wf.dat','w') as f:
    f.write("name sharpe\nIS 0.54\nOOS 0.00\n")
print("figdata17 wrote:", sorted(os.listdir(out))[-4:])
