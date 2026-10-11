"""Proper scoring rules: log and Brier. Proper = truth-telling is optimal."""
import numpy as np
def brier(p,y): return (p-y)**2
def logscore(p,y): return np.log(p if y==1 else 1-p)
rng=np.random.default_rng(5)
# true prob q=0.6 event; compare expected score of reporting p vs truth q
q=0.6
for p in (0.3,0.5,0.6,0.7,0.9):
    eb=q*brier(p,1)+(1-q)*brier(p,0)
    el=q*logscore(p,1)+(1-q)*logscore(p,0)
    print(f"q=0.6 report {p}: E[Brier]={eb:.4f}  E[log]={el:.4f}")
print("proper: best report = truth 0.6 for both rules")
