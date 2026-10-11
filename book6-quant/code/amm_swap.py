"""Constant-product AMM: swap output and price impact."""
def swap(dx, x, y, fee=0.003):
    dxf=dx*(1-fee); return dxf*y/(x+dxf)
x,y=1000.0,50000.0  # 1 token = 50 USD
print(f"pool x={x} y={y} price={y/x:.2f}")
for dx in (1,10,50,200,500):
    out=swap(dx,x,y); eff=out/dx; spot_after=(y-out)/(x+dx)
    print(f"in {dx:>4}: out {out:8.1f}  eff price {eff:6.2f}  "
          f"impact {1-eff/50:+.2%}  new px {spot_after:7.2f}")
