# code/ch05/forest_lib.py -- single tree vs forest + bootstrap variance.
# Run from the repository root:  python3 code/ch05/forest_lib.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = load_digits(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)

# --- variance of one tree over 20 bootstrap refits ----------------------
rng = np.random.default_rng(3)
accs = []
for b in range(20):
    bi = rng.choice(len(Xtr), len(Xtr), replace=True)
    m = DecisionTreeClassifier(random_state=b).fit(Xtr[bi], ytr[bi])
    accs.append(m.score(Xte, yte))
accs = np.array(accs)
print(f"single tree over 20 bootstraps: mean acc {accs.mean():.3f}  "
      f"sd {accs.std():.3f}  (min {accs.min():.3f}, max {accs.max():.3f})")

# --- depth sweep: where does a lone tree peak? --------------------------
print(f"\n{'depth':>6} {'train':>7} {'test':>7}")
for dp in [2, 4, 6, 10, None]:
    m = DecisionTreeClassifier(max_depth=dp, random_state=7).fit(Xtr, ytr)
    print(f"{str(dp):>6} {m.score(Xtr, ytr):>7.3f} {m.score(Xte, yte):>7.3f}")

# --- the ensemble --------------------------------------------------------
rf = RandomForestClassifier(300, random_state=7, n_jobs=-1).fit(Xtr, ytr)
full = DecisionTreeClassifier(random_state=7).fit(Xtr, ytr)
print(f"\nfull tree    test acc {full.score(Xte, yte):.3f}")
print(f"300-tree RF  test acc {rf.score(Xte, yte):.3f}   "
      f"OOB-free, no tuning")
