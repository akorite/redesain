import sys; sys.path.insert(0,'.')
from engine import load_bars, backtest, metrics
bars = load_bars("data/btc_daily.csv")
def sma(i,bars,w):
    if i+1<w: return sum(b[4] for b in bars[:i+1])/(i+1)
    return sum(b[4] for b in bars[i-w+1:i+1])/w
def strat(i,bars):
    if i<61: return 0
    return 1 if sma(i,bars,20)>sma(i,bars,60) else -1
print("fee sensitivity of SMA(20,60) long/short on 721 BTC daily bars")
for f in [0,5,10,25,50]:
    res = backtest(bars, strat, fee_bp=f, slip_bp=2)
    m = metrics(res.eq)
    print(f"fee {f:2d}bp: ret {m['ret']*100:+7.1f}%  sharpe {m['sharpe']:+.2f}  mdd {m['mdd']*100:.1f}%  trades {res.trades}")
