import pandas as pd, numpy as np
t = pd.read_csv("data/btc_daily.csv")
r = np.log(t["c"]).diff().dropna().values
sig_ann = pd.Series(r).rolling(20).std().shift(1).values*np.sqrt(365)
tgt = 0.40
lev = np.minimum(tgt/np.where(sig_ann>0.01, sig_ann, np.inf), 2.0)
lev = np.nan_to_num(lev, nan=0.0)
port = lev*r
def stats(x, name, lv=None):
    eq = np.exp(np.nancumsum(x))
    mdd = np.min(eq/np.maximum.accumulate(eq)-1)*100
    sh = np.nanmean(x)/np.nanstd(x)*np.sqrt(365)
    ann_vol = np.nanstd(x)*np.sqrt(365)*100
    tail = f"  mean lev {lv:.2f}" if lv is not None else ""
    print(f"{name:>14}: annvol {ann_vol:5.1f}%  sharpe {sh:+.2f}  mdd {mdd:.0f}%{tail}")
stats(r, "buy&hold")
stats(port, "vol-tgt", np.nanmean(lev))
# realized vol distribution check
realized = pd.Series(port).rolling(60).std().dropna().values*np.sqrt(365)
print(f"realized vol of targeted port: mean {realized.mean()*100:.0f}%  sd {realized.std()*100:.0f}% (target 40%)")
