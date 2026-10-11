# figures/fig_ch03_roc_steps.py -- ROC curve built from real scores.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                    random_state=7, stratify=y)
m = LogisticRegression(max_iter=5000).fit(Xtr, ytr)
s = m.decision_function(Xte)
fpr, tpr, thr = roc_curve(yte, s)
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.4))
ax = axes[0]
ax.hist(s[yte == 0], bins=18, alpha=0.7, color="#1F3A68",
        label="negatives (malignant)")
ax.hist(s[yte == 1], bins=18, alpha=0.7, color="#8A4B08",
        label="positives (benign)")
for t in [-1.5, 0.0, 1.5]:
    ax.axvline(t, color="k", ls="--", lw=0.8)
ax.set_xlabel("model score $f(\\mathbf{x})$"); ax.set_ylabel("count")
ax.legend(fontsize=8); ax.set_title("slide the threshold $\\tau$")
ax = axes[1]
ax.plot(fpr, tpr, "-", color="#1F3A68", lw=1.6)
for t, mk in [(-1.5, "o"), (0.0, "s"), (1.5, "^")]:
    i = np.argmin(np.abs(thr - t))
    ax.plot(fpr[i], tpr[i], mk, color="#8A4B08", ms=8,
            label=f"$\\tau\\approx{t:.1f}$")
ax.plot([0, 1], [0, 1], "k--", lw=0.8)
ax.set_xlabel("false-positive rate"); ax.set_ylabel("true-positive rate")
ax.set_title(f"ROC (AUC = {auc(fpr, tpr):.3f})")
ax.legend(fontsize=8, loc="lower right")
fig.tight_layout()
fig.savefig("figures/ch03/roc_steps.pdf")
print("wrote figures/ch03/roc_steps.pdf")
