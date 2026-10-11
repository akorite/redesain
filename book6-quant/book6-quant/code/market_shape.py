import json, numpy as np
m = json.load(open("data/pm_markets.json"))
sums, vols, prices = [], [], []
for x in m:
    try:
        pr = json.loads(x["outcomePrices"]) if isinstance(x["outcomePrices"],str) else x["outcomePrices"]
        pr = [float(v) for v in pr]
        if len(pr)==2:
            sums.append(sum(pr)); prices.append(pr[0])
            vols.append(float(x.get("volume24hr") or 0))
    except Exception: pass
sums = np.array(sums); prices = np.array(prices); vols = np.array(vols)
print(f"binary markets: {len(sums)}")
print(f"YES+NO sum: min {sums.min():.4f}  max {sums.max():.4f}  >1.03: {(sums>1.03).sum()}")
print(f"within 3c of 1.00: {(np.abs(sums-1)<=0.03).mean()*100:.0f}%")
print(f"extreme pricing: {(prices<0.05).sum()} markets YES<5c, {(prices>0.95).sum()} YES>95c")
print(f"24h volume: median ${np.median(vols):,.0f}  top ${vols.max():,.0f}")
print(f"liquidity-weighted mispricing proxy |sum-1| mean {np.abs(sums-1).mean():.4f}")
