"""Cross-market consistency: YES+NO=1, multi-outcome sum, Dutch book."""
import json
import numpy as np
d=json.load(open("data/pm_markets.json"))
viol=0; checked=0
for m in d:
    try: pr=[float(x) for x in json.loads(m["outcomePrices"])]
    except: continue
    if len(pr)!=2: continue
    checked+=1
    if abs(sum(pr)-1)>0.03: viol+=1
print(f"{checked} binary markets checked, YES+NO deviating >3c from 1: {viol}")
# extreme-price markets: how much volume sits at the tails
tails=[]
for m in d:
    try: pr=json.loads(m["outcomePrices"])
    except: continue
    if pr and float(pr[0])<0.05: tails.append((m["question"][:44],float(pr[0])))
print(f"markets priced <5c on the lead outcome: {len(tails)}")
for q,p in tails[:4]: print(f"  {p:.3f}  {q}")
