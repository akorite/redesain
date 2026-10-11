# figures/fig_ch06_scaling.py -- k-means before/after standardising.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X, y = load_wine(return_X_y=True)
j = [12, 0]                                   # proline + alcohol (unit gap)
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3))
for ax, Xs, ttl in [(axes[0], X[:, j], "raw units"),
                    (axes[1], StandardScaler().fit_transform(X[:, j]),
                     "standardised")]:
    z = KMeans(3, n_init=10, random_state=7).fit_predict(Xs)
    ax.scatter(Xs[:, 0], Xs[:, 1], c=z, s=13, cmap="Set1")
    ax.set_title(f"k-means k=3 on {ttl}")
    ax.set_xlabel("proline"); ax.set_ylabel("alcohol")
axes[0].annotate("proline's scale (300-1700)\ndrowns alcohol's (11-15):\nthe split is a unit artefact",
                 fontsize=8, color="#8A4B08", xy=(1000, 13.4))
fig.tight_layout()
fig.savefig("figures/ch06/scaling.pdf")
print("wrote figures/ch06/scaling.pdf")
