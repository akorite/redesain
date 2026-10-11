import numpy as np
# for a strategy with per-trade edge e and cost c per round-trip,
# how many trades does the Sharpe need to survive cost?
print("breakeven annualised edge needed to cover cost drag:")
print("(edge per year = trades/yr * cost)")
for t in [10,50,200,500]:
    for c in [0.001,0.005,0.01]:
        drag = t*c
        print(f"  {t} tr/yr @ {c*100:.1f}% cost: needs {drag*100:.1f}%/yr gross edge just to break even")
print("rule: gross sharpe needed ~= drag/vol -- high-turnover needs high Sharpe or low cost")
