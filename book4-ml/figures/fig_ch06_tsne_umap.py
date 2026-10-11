# figures/fig_ch06_tsne_umap.py -- t-SNE vs UMAP vs the honest caveat.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import umap

X, y = load_digits(return_X_y=True)
X2 = X[::2]; y2 = y[::2]                      # 898 pts, faster
Zt = TSNE(2, random_state=7, init="pca").fit_transform(X2)
Zu = umap.UMAP(n_components=2, random_state=7).fit_transform(X2)

fig, axes = plt.subplots(1, 2, figsize=(9.8, 3.6))
for ax, Z, ttl in [(axes[0], Zt, "t-SNE"),
                   (axes[1], Zu, "UMAP")]:
    for c in range(10):
        ax.scatter(Z[y2 == c, 0], Z[y2 == c, 1], s=7, label=str(c),
                   cmap="tab10")
    ax.set_title(ttl); ax.set_xticks([]); ax.set_yticks([])
axes[0].legend(fontsize=6, ncol=5, loc="lower center", framealpha=0.8)
fig.suptitle("local clusters are real; *distances between* clusters are "
             "not --- a 0.99 ARI here would still not certify structure",
             fontsize=9)
fig.tight_layout()
fig.savefig("figures/ch06/tsne_umap.pdf")
print("wrote figures/ch06/tsne_umap.pdf")
