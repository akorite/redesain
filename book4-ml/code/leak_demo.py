# code/ch03/leak_demo.py -- two leaks, two sizes, both measured.
# (a) Scale on the FULL data before splitting -- the textbook example.
# (b) Test rows inside the training set -- the guaranteed phantom.
# Run from the repository root:  python3 code/ch03/leak_demo.py
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_breast_cancer(return_X_y=True)
ks = np.arange(1, 30, 2)

# --- (a) standardise-then-split vs split-then-standardise --------------
Xs = (X - X.mean(0)) / X.std(0)              # scaler has seen the test rows
Xtr, Xte, ytr, yte = train_test_split(
    Xs, y, test_size=0.2, random_state=7, stratify=y)
leaky = max((KNeighborsClassifier(k).fit(Xtr, ytr).score(Xte, yte), k)
            for k in ks)

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=7, stratify=y)
mu, sd = Xtr.mean(0), Xtr.std(0)
honest = max((KNeighborsClassifier(k).fit((Xtr - mu) / sd, ytr)
              .score((Xte - mu) / sd, yte), k) for k in ks)
print(f"(a) scale->split {leaky[0]:.3f} at k={leaky[1]}   "
      f"split->scale {honest[0]:.3f} at k={honest[1]}   "
      f"diff {(leaky[0]-honest[0])*100:+.1f} pp")
print("    tiny here: iid rows share statistics, so the leaked scaler")
print("    barely differs from the honest one. Leak size is not fixed --")
print("    it scales with how much test information the step consumed.")

# --- (b) test rows copied into training --------------------------------
print("\n(b) fraction of test set duplicated into training:")
for frac in [0.0, 0.1, 0.25, 0.5]:
    n_leak = int(frac * len(Xte))
    Xtr_l = np.vstack([Xtr, Xte[:n_leak]])   # test rows join training!
    ytr_l = np.concatenate([ytr, yte[:n_leak]])
    m = KNeighborsClassifier(1).fit(Xtr_l, ytr_l)
    acc = m.score(Xte, yte)
    print(f"    {frac:.0%} leaked -> 1-NN test acc {acc:.3f}")
print("    1-NN answers each leaked row with itself: distance 0, label")
print("    memorised. Every leak ultimately works this way -- the model")
print("    is given an answer key, and 'accuracy' stops meaning anything.")
