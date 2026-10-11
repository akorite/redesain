import json, numpy as np
m = json.load(open("data/pm_markets.json"))
sp=[]; lock=[]
for x in m:
    bb,ba = x.get("bestBid"), x.get("bestAsk")
    if bb is None or ba is None: continue
    bb,ba=float(bb),float(ba)
    if not (ba>bb>0): continue
    sp.append(ba-bb)
    # ask-side YES+NO cost of guaranteed $1: ba + (1-bb)
    lock.append(ba + (1-bb))
sp=np.array(sp); lock=np.array(lock)
print(f"markets with a live two-sided book: {len(sp)}/100")
print(f"bid-ask width: median {np.median(sp)*100:.1f}c mean {sp.mean()*100:.1f}c")
print(f"tightest {sp.min()*100:.1f}c widest {sp.max()*100:.1f}c")
print(f"YES+NO bought at ask: median ${np.median(lock):.3f}  <$0.99: {(lock<0.99).sum()}  >$1.01: {(lock>1.01).sum()}")
print(f"cheapest lock cost ${lock.min():.3f} -> guaranteed ${1-lock.min():+.3f} per $1")
