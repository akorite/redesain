import json, numpy as np
m = json.load(open("data/pm_markets.json"))
# Brier score of the market's own price if we treated it as forecast vs outcomes
# unresolved markets can't be scored; use price-vs-50c divergence as "conviction surface"
conv = []
for x in m:
    try:
        pr = json.loads(x["outcomePrices"]) if isinstance(x["outcomePrices"],str) else x["outcomePrices"]
        p = float(pr[0])
        conv.append(abs(p-0.5)*2)  # 0=no opinion, 1=certain
    except Exception: pass
conv = np.array(conv)
print(f"conviction |2p-1| over {len(conv)} binary markets")
print(f"mean {conv.mean():.3f}   >0.9: {(conv>0.9).sum()}   <0.1: {(conv<0.1).sum()}")
# expected Brier of a 50c baseline vs market conviction
brier50 = 0.25
# if market were perfectly calibrated, E[brier|p]=p(1-p); compare
e_brier = np.mean([p*(1-p) for p in conv/2+0.5])
print(f"E[Brier] if market calibrated = {e_brier:.4f} vs 50c baseline {brier50}")
print(f"info gain over coin-flip = {(1-e_brier/brier50)*100:.0f}%")
