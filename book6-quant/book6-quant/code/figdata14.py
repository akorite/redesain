import csv, math
import statistics as st
r=[]
with open("data/btc_daily.csv") as fh:
    rd=csv.reader(fh); next(rd)
    px=[float(row[4]) for row in rd]
r=[math.log(px[i]/px[i-1]) for i in range(1,len(px))]
h,edges=[0]*40,[0]*41
mn,mx=min(r),max(r); w=(mx-mn)/40
for x in r: h[min(39,int((x-mn)/w))]+=1
for i in range(41): edges[i]=mn+i*w
with open("../figures/data/RHIST.tex","w") as fh:
    for i in range(40): fh.write(f"{(edges[i]+edges[i+1])/2:.4f} {h[i]}\n")
# normal curve overlay at same scale
mu,sd=st.mean(r),st.stdev(r)
import math as m
with open("../figures/data/NCURVE.tex","w") as fh:
    for i in range(80):
        x=mn+i*(mx-mn)/80
        fh.write(f"{x:.4f} {len(r)*w/(sd*m.sqrt(2*m.pi))*m.exp(-((x-mu)/sd)**2/2):.1f}\n")
# sorted tail
rs=sorted(r)
with open("../figures/data/TAILZ.tex","w") as fh:
    for i in range(60): fh.write(f"{i} {rs[i]*100:.2f}\n")
print("ok")
