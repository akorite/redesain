# figures/fig_ch03_biasvariance.py -- train/test accuracy vs k (real sweep).
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier

X, y = load_digits(return_X_y=True)
rng = np.random.default_rng(11)
perm = rng.permutation(len(y)); tr, te = perm[:1400], perm[1400:]
ks = [1, 2, 3, 5, 8, 11, 15, 20, 25, 35, 50, 75, 100]
tr_acc, te_acc = [], []
for k in ks:
    m = KNeighborsClassifier(k).fit(X[tr], y[tr])
    tr_acc.append(m.score(X[tr], y[tr])); te_acc.append(m.score(X[te], y[te]))

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.semilogx(ks, tr_acc, "o-", color="#8A4B08", label="train accuracy")
ax.semilogx(ks, te_acc, "s-", color="#1F3A68", label="test accuracy")
ax.fill_between(ks, tr_acc, te_acc, color="grey", alpha=0.15)
ax.annotate("complex model:\nmemorises", xy=(1, 1.0), xytext=(1.3, 0.90),
            fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
ax.annotate("stable model:\ngeneralises", xy=(25, 0.947), xytext=(30, 0.91),
            fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
ax.set_xlabel("$k$ of kNN (smaller = more complex)")
ax.set_ylabel("accuracy")
ax.set_ylim(0.86, 1.02)
ax.legend(fontsize=8, loc="lower left")
fig.tight_layout()
fig.savefig("figures/ch03/biasvariance.pdf")
print("wrote figures/ch03/biasvariance.pdf")
