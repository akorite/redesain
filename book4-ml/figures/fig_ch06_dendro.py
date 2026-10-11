# figures/fig_ch06_dendro.py -- wine dendrograms: ward vs single linkage.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True)
X = StandardScaler().fit_transform(X)
fig, axes = plt.subplots(1, 2, figsize=(10.6, 3.4))
for ax, meth in zip(axes, ["ward", "single"]):
    Z = linkage(X, method=meth)
    dendrogram(Z, ax=ax, no_labels=True, color_threshold=None,
               above_threshold_color="#1F3A68")
    ax.set_title(f"{meth} linkage")
    ax.set_xlabel("sample"); ax.set_ylabel("merge distance")
axes[0].axhline(7, color="#8A4B08", ls="--", lw=0.9)
axes[0].annotate("cut here -> 3 groups", xy=(140, 7.4), fontsize=8,
                 color="#8A4B08")
axes[1].annotate("chaining: one long tail,\nno clean cut", xy=(60, 1.1),
                 fontsize=8, color="#8A4B08")
fig.tight_layout()
fig.savefig("figures/ch06/dendro.pdf")
print("wrote figures/ch06/dendro.pdf")
