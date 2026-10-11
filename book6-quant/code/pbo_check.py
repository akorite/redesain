import numpy as np
# CSCV-lite: 4 folds; each fold picks best IS strategy, measure its OOS rank.
rng = np.random.default_rng(7)
days, S = 720, 60
# one WEAK edge among 59 noise strategies -- the realistic case
true_sharpe = np.zeros(S); true_sharpe[3] = 0.15
rets = rng.normal(0, 1/np.sqrt(252), (days, S)) + true_sharpe/np.sqrt(252)
folds = 4; rank_in_oos = []
for f in range(folds):
    tr = np.ones(days, bool); tr[f*days//folds:(f+1)*days//folds] = False
    is_sh = rets[tr].mean(0)/rets[tr].std(0)
    oos_sh = rets[~tr].mean(0)/rets[~tr].std(0)
    pick = is_sh.argmax()
    rank = (oos_sh > oos_sh[pick]).sum()
    rank_in_oos.append(rank/(S-1))
    print(f"fold {f}: IS pick strat {pick:2d} -> OOS rank {rank}/{S-1} ({rank/(S-1):.2f})")
pbo = np.mean([r>0.5 for r in rank_in_oos])
print(f"PBO = {pbo:.2f}  (IS-best lands below OOS median this often)")
# control: NO real edge at all
rets2 = rng.normal(0, 1/np.sqrt(252), (days, S))
r2=[]
for f in range(folds):
    tr = np.ones(days, bool); tr[f*days//folds:(f+1)*days//folds] = False
    i2 = rets2[tr].mean(0)/rets2[tr].std(0); o2 = rets2[~tr].mean(0)/rets2[~tr].std(0)
    r2.append((o2>o2[i2.argmax()]).sum()/(S-1))
print(f"no-edge control PBO = {np.mean([r>0.5 for r in r2]):.2f}")
