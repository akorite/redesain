import pandas as pd, numpy as np, json, os
os.makedirs("../figures/data", exist_ok=True)
t = pd.read_csv("data/btc_daily.csv")
r = np.log(t["c"]).diff().dropna().values
# 1. autocorr bars
ar=np.abs(r)
with open("../figures/data/ch16_autocorr.dat","w") as fh:
    for k in [1,2,5,10,15,20]:
        fh.write(f"{k} {np.corrcoef(ar[k:],ar[:-k])[0,1]:.4f} {np.corrcoef(r[k:],r[:-k])[0,1]:.4f}\n")
# 2. vol-target leverage series
sig_ann = pd.Series(r).rolling(20).std().shift(1).values*np.sqrt(365)
lev = np.minimum(0.40/np.where(sig_ann>0.01,sig_ann,np.inf),2.0)
with open("../figures/data/ch16_lev.dat","w") as fh:
    for i,v in enumerate(lev): fh.write(f"{i} {0.0 if np.isnan(v) else v:.4f}\n")
# 3. dd curves
eq=np.exp(np.nancumsum(r)); pk=np.maximum.accumulate(eq); dd=eq/pk-1
size=np.ones(len(r)); st_=1.0
for i in range(1,len(r)):
    if dd[i]<-0.20: st_=0.0
    elif dd[i]<-0.10: st_=min(st_,0.5)
    elif dd[i]>-0.05: st_=min(1.0,st_*1.1)
    size[i]=st_
eq2=np.exp(np.nancumsum(size*r)); dd2=eq2/np.maximum.accumulate(eq2)-1
with open("../figures/data/ch16_dd.dat","w") as fh:
    for i in range(0,len(r),4): fh.write(f"{i} {dd[i]*100:.2f} {dd2[i]*100:.2f}\n")
# 4-5. capstone equity curves + rp weights
f=json.load(open("data/hl_funding_btc.json"))
hourly=np.array([float(x['fundingRate']) for x in f])
d=len(hourly)//24; carry=hourly[:d*24].reshape(d,24).sum(1)
eqs=np.exp(np.nancumsum(r[:d])); eqc=np.exp(np.nancumsum(carry))
va=r[:d].std(); vb=carry.std(); wa,wb=(1/va),(1/vb); s=wa+wb; wa,wb=wa/s,wb/s
eqp=np.exp(np.nancumsum(wa*r[:d]+wb*carry))
with open("../figures/data/ch16_eq.dat","w") as fh:
    for i in range(d): fh.write(f"{i} {eqs[i]:.4f} {eqc[i]:.4f} {eqp[i]:.4f}\n")
with open("../figures/data/ch16_weights.dat","w") as fh:
    fh.write(f"mom 0.333 0.221 0.333\n car 0.333 0.694 0.333\n mkt 0.333 0.085 0.333\n")
# 6. weekend/weekday vol bars (reuse calendar_risk numbers)
t2=pd.to_datetime(t["time"],unit="s"); dow=t2.dt.dayofweek[1:]
with open("../figures/data/ch16_wkvol.dat","w") as fh:
    for d_ in range(7):
        v=r[dow==d_].std()*np.sqrt(365)*100
        fh.write(f"{d_} {v:.1f}\n")
print("figdata16: 6 dat files written")
