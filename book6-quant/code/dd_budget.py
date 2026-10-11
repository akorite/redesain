import pandas as pd, numpy as np
t = pd.read_csv("data/btc_daily.csv")
r = np.log(t["c"]).diff().dropna().values
eq = np.exp(np.nancumsum(r))
peak = np.maximum.accumulate(eq)
dd = eq/peak-1
# budget rule: kill the position when dd breaches -25%, re-enter at new peak... simpler: measure time under water
tuw = (dd<-0.10).sum()
print(f"buy&hold: days {len(r)}  maxDD {dd.min()*100:.0f}%  days under -10%: {tuw} ({tuw/len(r)*100:.0f}%)")
# budget variant: halve size when dd<-10%, flat below -20% (state machine on real tape)
size=np.ones(len(r)); st=1.0
for i in range(1,len(r)):
    if dd[i]<-0.20: st=0.0
    elif dd[i]<-0.10: st=min(st,0.5)
    elif dd[i]>-0.05: st=min(1.0,st*1.1)
    size[i]=st
p = size*r
eq2=np.exp(np.nancumsum(p)); dd2=eq2/np.maximum.accumulate(eq2)-1
print(f"dd-budget:  maxDD {dd2.min()*100:.0f}%  days under -10%: {(dd2<-0.10).sum()}  final eq {eq2[-1]:.2f} vs {eq[-1]:.2f}")
