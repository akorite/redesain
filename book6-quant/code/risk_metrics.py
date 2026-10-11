import csv, math
r=[]
with open("data/btc_daily.csv") as fh:
    rd=csv.reader(fh); next(rd)
    px=[float(row[4]) for row in rd]
r=[math.log(px[i]/px[i-1]) for i in range(1,len(px))]
r.sort()
n=len(r)
import statistics as st
mu,sd=st.mean(r),st.stdev(r)
def var_es(q):
    v=r[int(q*n)]
    es=sum(x for x in r if x<=v)/max(1,sum(1 for x in r if x<=v))
    return v,es
for q in (0.05,0.01):
    v,es=var_es(q)
    # normal-equivalent
    from scipy.stats import norm
    vn=mu+norm.ppf(q)*sd; en=mu-sd*norm.pdf(norm.ppf(q))/q
    print(f"{q:.0%}: hist VaR {v*100:+.2f}%  ES {es*100:+.2f}%   normal VaR {vn*100:+.2f}%  ES {en*100:+.2f}%")
k=sum(1 for x in r if abs(x)>3*sd)
print(f"n={n}  |r|>3sd: {k} days ({k/n:.1%})   normal expect {2*0.00135*n:.1f} days")
