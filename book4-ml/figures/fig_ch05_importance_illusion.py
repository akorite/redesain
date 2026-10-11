# figures/fig_ch05_importance_illusion.py -- MDI vs permutation importance
# with a correlated duplicate planted to dilute the real signal.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names
# plant a diluted copy of the most important feature
best = int(np.argmax([abs(np.corrcoef(X[:, j], y)[0, 1]) for j in range(30)]))
X2 = np.c_[X, X[:, best] + np.random.default_rng(0).normal(0, 0.5, len(y))]
names2 = list(names) + ["worst area (noisy dup)"]

Xtr, Xte, ytr, yte = train_test_split(X2, y, test_size=0.25,
                                    random_state=7, stratify=y)
rf = RandomForestClassifier(200, random_state=7, n_jobs=-1).fit(Xtr, ytr)
mdi = rf.feature_importances_
perm = permutation_importance(rf, Xte, yte, n_repeats=10,
                              random_state=7).importances_mean

top = np.argsort(perm)[-6:]
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.2))
axes[0].barh([names2[i][:18] for i in top], mdi[top], color="#1F3A68")
axes[0].set_title("impurity importance (MDI)"); axes[0].set_xlabel("MDI")
axes[1].barh([names2[i][:18] for i in top], perm[top], color="#8A4B08")
axes[1].set_title("permutation importance (test)"); axes[1].set_xlabel("drop in acc")
fig.suptitle("a noisy duplicate splits the vote: MDI spreads credit, "
             "permutation keeps score", fontsize=10)
fig.tight_layout()
fig.savefig("figures/ch05/importance_illusion.pdf")
print("planted dup of:", names[best])
print("wrote figures/ch05/importance_illusion.pdf")
