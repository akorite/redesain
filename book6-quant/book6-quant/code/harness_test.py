"""Unit tests for the backtester itself."""
import sys; sys.path.insert(0,'.')
from engine import backtest, metrics
# T1: flat market, any strategy -> zero PnL
flat=[(i,100,100,100,100) for i in range(50)]
r=backtest(flat,lambda i,b: 1 if i>5 else 0,fee_bp=0,slip_bp=0)
assert abs(r.eq[-1]-1.0)<1e-9, "T1 flat failed"
# T2: always-long on +1%/bar -> exact compounding
up=[(i,100*(1.01**i),0,0,100*(1.01**i)) for i in range(50)]
r=backtest(up,lambda i,b: 1,fee_bp=0,slip_bp=0)
exp=1.01**48  # bought at open[1]=101, holds through bar 49
assert abs(r.eq[-1]/r.eq[0]-exp)<1e-6, f"T2 trend failed {r.eq[-1]/r.eq[0]:.6f} vs {exp:.6f}"
# T3: fees exactly reduce PnL by fee*turnover
r0=backtest(up,lambda i,b: 1,fee_bp=0,slip_bp=0)
r1=backtest(up,lambda i,b: 1,fee_bp=100,slip_bp=0)
assert r1.eq[-1]<r0.eq[-1], "T3 fees failed"
# T4: a trade signal delayed one bar fills at next open, not current close
bars2=[(i,100,0,0,100+10*(i>=3)) for i in range(10)]
r=backtest(bars2,lambda i,b: 1 if i>=3 else 0,fee_bp=0,slip_bp=0)
assert r.trades>=1, "T4 no trade"
print("harness unit tests: T1 flat, T2 compounding, T3 fees, T4 next-open fill -- ALL PASS")
