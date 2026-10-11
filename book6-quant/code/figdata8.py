import sys; sys.path.insert(0,'.')
from engine import load_bars, backtest, metrics
bars=load_bars("data/btc_daily.csv")
def sma(i,w):
    return sum(b[4] for b in bars[i-w+1:i+1])/w if i+1>=w else sum(b[4] for b in bars[:i+1])/(i+1)
def strat(i,bars):
    if i<61: return 0
    return 1 if sma(i,20)>sma(i,60) else -1
res=backtest(bars,strat,fee_bp=5,slip_bp=2)
with open("/tmp/E_SMA.tex","w") as fh:
    for i,e in enumerate(res.eq): fh.write(f"{i} {e:.4f}\n")
with open("/tmp/E_BH.tex","w") as fh:
    for i,b in enumerate(bars): fh.write(f"{i} {b[4]/bars[0][4]:.4f}\n")
def leaky(i,bars):
    r=bars[i+1][4]/bars[i][4]-1
    return 1 if r>0 else -1
res2=backtest(bars,leaky,fee_bp=5,slip_bp=2)
with open("/tmp/E_LEAK.tex","w") as fh:
    for i,e in enumerate(res2.eq): fh.write(f"{i} {e:.4f}\n")
# drawdown of sma
peak=res.eq[0]
with open("/tmp/D_SMA.tex","w") as fh:
    for i,e in enumerate(res.eq):
        peak=max(peak,e); fh.write(f"{i} {(e/peak-1)*100:.2f}\n")
print("figs done", len(res.eq))
