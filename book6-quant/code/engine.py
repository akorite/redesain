"""A 70-line event-driven backtester.
Bars -> strategy.signal -> fill at NEXT bar open - fees - slippage.
Position = fraction of equity (-1..+1 = up to 100% notional)."""
import csv, math

def load_bars(path):
    rows=[]
    with open(path) as fh:
        r=csv.reader(fh); next(r)
        for t,o,h,l,c in r: rows.append((int(t),float(o),float(h),float(l),float(c)))
    return rows

class Result:
    def __init__(s): s.eq=[1.0]; s.trades=0

def backtest(bars, strategy, fee_bp=5, slip_bp=2, cash0=1.0):
    """strategy(i,bars)->target fraction {-1,0,+1}; filled at open[i+1]."""
    res=Result(); cash=cash0; units=0.0; cur_frac=0.0
    for i in range(len(bars)-1):
        tgt_frac = strategy(i, bars)
        if tgt_frac != cur_frac:
            o2 = bars[i+1][1]
            eq_now = cash + units*bars[i+1][4]
            tgt_units = tgt_frac*eq_now/o2
            dq = tgt_units - units
            px = o2*(1+slip_bp*1e-4*(1 if dq>0 else -1))
            fee = abs(dq)*px*fee_bp*1e-4
            cash -= dq*px + fee
            units = tgt_units; cur_frac = tgt_frac
            res.trades += 1
        res.eq.append(cash + units*bars[i+1][4])
    return res

def metrics(eq):
    rets=[eq[i+1]/eq[i]-1 for i in range(len(eq)-1)]
    n=len(rets); mu=sum(rets)/n
    sd=(sum((r-mu)**2 for r in rets)/max(n-1,1))**0.5
    sharpe=mu/sd*math.sqrt(365) if sd>0 else 0
    peak=eq[0]; mdd=0
    for e in eq:
        peak=max(peak,e); mdd=min(mdd,e/peak-1)
    return {"ret":eq[-1]/eq[0]-1,"sharpe":sharpe,"mdd":mdd,"n":n}
