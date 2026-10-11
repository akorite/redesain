import sys; sys.path.insert(0,'.')
from engine import load_bars, backtest, metrics
bars = load_bars("data/btc_daily.csv")
def strat_donch(i,bars):
    if i<50: return 0
    hh = max(b[2] for b in bars[i-50:i])
    ll = min(b[3] for b in bars[i-50:i])
    c = bars[i][4]
    if c > hh*0.999: return 1
    if c < ll*1.001: return -1
    return None  # hold previous
prev=[0]
def s2(i,bars):
    v = strat_donch(i,bars)
    if v is None: return prev[0]
    prev[0]=v; return v
r1=backtest(bars,s2,fee_bp=5,slip_bp=2); m1=metrics(r1.eq)
print(f"Donchian(50) breakout: ret {m1['ret']*100:+.1f}%  sharpe {m1['sharpe']:+.2f}  mdd {m1['mdd']*100:.1f}%  trades {r1.trades}")
def rsi(i,bars):
    if i<15: return 0
    ds=[bars[k+1][4]-bars[k][4] for k in range(i-14,i)]
    up=sum(d for d in ds if d>0)/14; dn=-sum(d for d in ds if d<0)/14 or 1e-9
    rs=100-100/(1+up/dn)
    return -1 if rs>70 else (1 if rs<30 else 0)
r2=backtest(bars,rsi,fee_bp=5,slip_bp=2); m2=metrics(r2.eq)
print(f"RSI(14) mean-rev:    ret {m2['ret']*100:+.1f}%  sharpe {m2['sharpe']:+.2f}  mdd {m2['mdd']*100:.1f}%  trades {r2.trades}")
print("same harness, same data, same fees -- the strategy is the only variable")
