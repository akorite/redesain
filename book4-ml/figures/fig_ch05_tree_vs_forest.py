# figures/fig_ch05_tree_vs_forest.py -- boundary: one tree vs forest (2-D).
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=260, n_features=2, n_redundant=0,
                           n_informative=2, n_clusters_per_class=1,
                           flip_y=0.05, random_state=8)
xx, yy = np.meshgrid(np.linspace(X[:,0].min()-0.5, X[:,0].max()+0.5, 220),
                     np.linspace(X[:,1].min()-0.5, X[:,1].max()+0.5, 220))
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.3), sharey=True)
for ax, m, ttl in [(axes[0], DecisionTreeClassifier(random_state=7),
                    "one tree"),
                   (axes[1], RandomForestClassifier(200, random_state=7,
                                                  n_jobs=-1),
                    "200-tree forest")]:
    m.fit(X, y)
    Z = m.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, levels=[-0.5, 0.5, 1.5],
                colors=["#dbe6f5", "#f5e0d8"], alpha=0.9)
    ax.scatter(X[y==0,0], X[y==0,1], s=12, c="#1F3A68")
    ax.scatter(X[y==1,0], X[y==1,1], s=12, c="#8A4B08", marker="s")
    ax.set_title(ttl + f" (train acc {m.score(X,y):.2f})")
axes[0].set_ylabel("$x_2$")
for ax in axes: ax.set_xlabel("$x_1$")
fig.suptitle("trees draw staircases; forests smooth them", fontsize=10)
fig.tight_layout()
fig.savefig("figures/ch05/tree_vs_forest.pdf")
print("wrote figures/ch05/tree_vs_forest.pdf")
