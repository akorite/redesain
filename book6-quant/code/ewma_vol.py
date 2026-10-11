import csv, math
r=[]
with open("data/btc_daily.csv") as fh:
    rd=csv.reader(fh); next(rd)
    px=[float(row[4]) for row in rd]
r=[math.log(px[i]/px[i-1]) for i in range(1,len(px))]
# EWMA lambda=0.94 vs 60d rolling
lam=0.94
ewma=[0.0]*len(r)
ewma[0]=r[0]**2
for i in range(1,len(r)):
    ewma[i]=lam*ewma[i-1]+(1-lam)*r[i]**2
import statistics as st
roll=[st.stdev(r[max(0,i-60):i+1]) if i>1 else abs(r[0]) for i in range(len(r))]
e_annual=[(math.sqrt(x*365))*100 for x in ewma]
r_annual=[x*math.sqrt(365)*100 for x in roll]
print(f"EWMA vol now {e_annual[-1]:.1f}%   60d rolling {r_annual[-1]:.1f}%")
print(f"EWMA range [{min(e_annual):.0f},{max(e_annual):.0f}]%   rolling range [{min(r_annual):.0f},{max(r_annual):.0f}]%")
print("EWMA reacts faster to shocks; rolling is smoother and staler")
with open("../figures/data/EWMA.tex","w") as fh:
    for i in range(0,len(r),5): fh.write(f"{i} {e_annual[i]:.1f}\n")
with open("../figures/data/ROLL.tex","w") as fh:
    for i in range(0,len(r),5): fh.write(f"{i} {r_annual[i]:.1f}\n")
