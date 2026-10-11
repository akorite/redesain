# figures/fig_ch05_ig_panel.py -- information-gain anatomy for one split.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
names = load_wine().feature_names
Xtr, _, ytr, _ = train_test_split(X, y, test_size=0.25,
                                 random_state=7, stratify=y)

def gini(labels):
    _, c = np.unique(labels, return_counts=True)
    p = c / len(labels)
    return 1 - (p ** 2).sum()

# the root split chosen by tree_scratch: color_intensity <= 3.8
L = Xtr[:, names.index("color_intensity")] <= 3.8
g_par, g_L, g_R = gini(ytr), gini(ytr[L]), gini(ytr[~L])
w = (L.sum() * g_L + (~L).sum() * g_R) / len(ytr)

fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.0))
for ax, lab, mask, g in [(axes[0], "root", np.ones(len(ytr), bool), g_par),
                         (axes[1], "left child (le 3.8)", L, g_L),
                         (axes[2], "right child (gt 3.8)", ~L, g_R)]:
    cnt = [int((ytr[mask] == c).sum()) for c in range(3)]
    ax.bar(["0", "1", "2"], cnt, color=["#1F3A68", "#8A4B08", "#1E5E3A"])
    ax.set_title(f"{lab}\nn={int(mask.sum())}, Gini={g:.3f}", fontsize=9)
    ax.set_ylim(0, 70)
    for i, v in enumerate(cnt):
        ax.text(i, v + 1, str(v), ha="center", fontsize=8)
fig.suptitle(f"weighted Gini {w:.3f} vs parent {g_par:.3f}  ->  "
             f"information gain {g_par - w:.4f}", fontsize=10)
fig.tight_layout()
fig.savefig("figures/ch05/ig_panel.pdf")
print("wrote figures/ch05/ig_panel.pdf")
