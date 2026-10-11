# figures/fig_ch03_knn_boundaries.py -- kNN decision boundaries at k=1,5,25.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier

X, y = make_classification(n_samples=220, n_features=2, n_redundant=0,
                           n_informative=2, n_clusters_per_class=1,
                           flip_y=0.06, random_state=3)
xx, yy = np.meshgrid(np.linspace(X[:,0].min()-0.5, X[:,0].max()+0.5, 220),
                     np.linspace(X[:,1].min()-0.5, X[:,1].max()+0.5, 220))
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.2), sharey=True)
for ax, k in zip(axes, [1, 5, 25]):
    m = KNeighborsClassifier(k).fit(X, y)
    Z = m.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, levels=[-0.5, 0.5, 1.5],
                colors=["#dbe6f5", "#f5e0d8"], alpha=0.9)
    ax.contour(xx, yy, Z, levels=[0.5], colors="k", linewidths=0.8)
    ax.scatter(X[y==0,0], X[y==0,1], s=14, c="#1F3A68", label="class 0")
    ax.scatter(X[y==1,0], X[y==1,1], s=14, c="#8A4B08", marker="s",
               label="class 1")
    ax.set_title(f"$k={k}$")
    ax.set_xlabel("$x_1$")
axes[0].set_ylabel("$x_2$")
axes[0].legend(loc="upper right", fontsize=8)
fig.tight_layout()
fig.savefig("figures/ch03/knn_boundaries.pdf")
print("wrote figures/ch03/knn_boundaries.pdf")
