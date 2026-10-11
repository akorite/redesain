"""Leakage demo: signal computed with tomorrow's close vs today's."""
import sys; sys.path.insert(0,'.')
from engine import load_bars, backtest, metrics
bars=load_bars("data/btc_daily.csv")
def leaky(i,bars):   # uses bars[i+1] — tomorrow's close, unknowable
    r=bars[i+1][4]/bars[i][4]-1
    return 1 if r>0 else -1
def honest(i,bars):  # momentum from today's close only
    r=bars[i][4]/bars[i-1][4]-1 if i>0 else 0
    return 1 if r>0 else (-1 if r<0 else 0)
l=metrics(backtest(bars,leaky,fee_bp=5,slip_bp=2).eq)
h=metrics(backtest(bars,honest,fee_bp=5,slip_bp=2).eq)
print(f"one-bar foresight (leak): ret {l['ret']*100:+.0f}% sharpe {l['sharpe']:+.2f} mdd {l['mdd']*100:.1f}%")
print(f"same-sign momentum (honest): ret {h['ret']*100:+.1f}% sharpe {h['sharpe']:+.2f} mdd {h['mdd']*100:.1f}%")
print("leak turns a coin-flip into a crystal ball; nothing here is tradeable")
