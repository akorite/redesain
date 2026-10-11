"""ch18 figure data -> ../figures/data/."""
import json, math, os
out='../figures/data'; os.makedirs(out,exist_ok=True)
f=json.load(open('data/hl_funding_btc.json'))
fr=[float(x['fundingRate']) for x in f]; prem=[float(x['premium']) for x in f]
carry=[fr[i]-(prem[i]-prem[i-1]) for i in range(1,len(fr))]
with open(f'{out}/ch18-premium.dat','w') as fh:
    for i,p in enumerate(prem): fh.write(f"{i} {p*1e4:.3f}\n")
eq=1.0
with open(f'{out}/ch18-carryeq.dat','w') as fh:
    for i,x in enumerate(carry):
        eq*=math.exp(x); fh.write(f"{i} {eq:.5f}\n")
with open(f'{out}/ch18-carry.dat','w') as fh:
    for i,x in enumerate(carry): fh.write(f"{i} {x*1e4:.3f}\n")
with open(f'{out}/ch18-tstat.dat','w') as fh:
    for n in (50,100,200,300,499):
        xs=carry[:n]; m=sum(xs)/n
        sd=math.sqrt(sum((a-m)**2 for a in xs)/(n-1)); se=sd/math.sqrt(n)
        fh.write(f"{n} {m/se:.2f}\n")
with open(f'{out}/ch18-liq.dat','w') as fh:
    fh.write("name buf\n2x 50\n3x 33\n5x 20\n")
print("figdata18 done")
