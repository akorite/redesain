# code/ch03/nb_scratch.py -- Gaussian naive Bayes in log-space on titanic.
# Numeric columns get Gaussian likelihoods; sex gets a categorical one.
# Run from the repository root:  python3 code/ch03/nb_scratch.py
import numpy as np
import pandas as pd

df = pd.read_csv("data/titanic.csv")
y = df.survived.values
Xn = df[["age", "fare"]].fillna(df[["age", "fare"]].median()).values
sex = df.sex.values

rng = np.random.default_rng(5)
perm = rng.permutation(len(y))
tr, te = perm[:700], perm[700:]

# --- fit: per-class mean/var of each numeric column + per-class sex rates ---
classes = np.unique(y)
log_prior = {c: np.log((y[tr] == c).mean()) for c in classes}
mu = {c: Xn[tr][y[tr] == c].mean(0) for c in classes}
var = {c: Xn[tr][y[tr] == c].var(0) + 1e-3 for c in classes}   # +eps for safety
sex_rate = {c: {s: (sex[tr][y[tr] == c] == s).mean()
                for s in np.unique(sex)} for c in classes}

def predict(i):
    x, s = Xn[i], sex[i]
    def loglik(c):
        ll = log_prior[c]
        ll += (-0.5 * np.log(2 * np.pi * var[c])
               - (x - mu[c]) ** 2 / (2 * var[c])).sum()
        ll += np.log(sex_rate[c][s] + 1e-9)
        return ll
    return max(classes, key=loglik)

pred = np.array([predict(i) for i in te])
tp = int(((pred == 1) & (y[te] == 1)).sum())
fp = int(((pred == 1) & (y[te] == 0)).sum())
fn = int(((pred == 0) & (y[te] == 1)).sum())
tn = int(((pred == 0) & (y[te] == 0)).sum())
print("confusion matrix (rows=true, cols=pred):")
print(f"            pred=0  pred=1")
print(f"  true=1      {fn:4d}    {tp:4d}")
print(f"  true=0      {tn:4d}    {fp:4d}")
print(f"\naccuracy {(pred == y[te]).mean():.3f}   "
      f"precision {tp/(tp+fp):.3f}   recall {tp/(tp+fn):.3f}")
