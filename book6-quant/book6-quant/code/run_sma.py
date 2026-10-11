"""SMA(20,60) cross on real BTC daily bars, honest fills."""
import sys; sys.path.insert(0,'.')
from engine import load_bars, backtest, metrics
bars=load_bars("data/btc_daily.csv")
def sma(i,bars,w):
    if i+1<w: return sum(b[4] for b in bars[:i+1])/(i+1)
    return sum(b[4] for b in bars[i-w+1:i+1])/w
def strat(i,bars):
    if i<61: return 0
    return 1 if sma(i,bars,20)>sma(i,bars,60) else -1
res=backtest(bars,strat,fee_bp=5,slip_bp=2)
m=metrics(res.eq)
bh=metrics([1.0]+[b[4]/bars[0][4] for b in bars])
print(f"bars {len(bars)}  trades {res.trades}")
print(f"SMA20/60: ret {m['ret']*100:+.1f}%  sharpe {m['sharpe']:+.2f}  mdd {m['mdd']*100:.1f}%")
print(f"buy&hold: ret {bh['ret']*100:+.1f}%  sharpe {bh['sharpe']:+.2f}  mdd {bh['mdd']*100:.1f}%")
