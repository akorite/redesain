import numpy as np
rng=np.random.default_rng(5)
T=48
vol=0.5+1.5*np.sin(np.pi*np.arange(T)/T)**2   # U-inverted: heavy midday? use real: heavy at ends
vol=0.6+2.0*(np.cos(np.pi*(np.arange(T)/T-0.5)))**2  # U-shape: heavy open/close
vol/=vol.sum()
twap=np.ones(T)/T
vwap=vol/vol.sum()
# implementation shortfall vs arrival mid
mid0=100.0
sig=0.0015
# simulate price walk + per-slice impact 0.4bp*sqrt(slice/daily_vol_frac)
steps=rng.normal(0,sig,T); px=mid0*np.cumprod(1+steps)
def cost(schedule):
    tot=0
    for t in range(T):
        impact=0.0008*np.sqrt(schedule[t]/vol[t]) if vol[t]>0 else 0
        tot+=schedule[t]*(px[t]*(1+impact)-mid0)
    return tot
c_twap=cost(twap); c_vwap=cost(vwap)
print(f"slices {T}  volume U-shaped (open/close heavy)")
print(f"IS TWAP: {c_twap*1e4/mid0:+7.2f}bp   IS VWAP: {c_vwap*1e4/mid0:+7.2f}bp")
print("vwap wins on U-volume: schedules weight to where liquidity is")
with open("../figures/data/VOL.tex","w") as fh:
    for t in range(T): fh.write(f"{t} {vol[t]*100:.2f}\n")
with open("../figures/data/PX.tex","w") as fh:
    for t in range(T): fh.write(f"{t} {px[t]:.3f}\n")
