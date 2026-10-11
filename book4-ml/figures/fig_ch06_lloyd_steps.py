# figures/fig_ch06_lloyd_steps.py -- Lloyd's algorithm in 4 panels.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(2)
X = np.vstack([rng.normal([2, 2], 0.5, (40, 2)),
               rng.normal([5, 1], 0.5, (40, 2)),
               rng.normal([3.5, 5], 0.6, (40, 2))])
k = 3
C = np.array([[1, 4.5], [6, 5], [2.5, 0]])
frames = []
for it in range(4):
    d = ((X[:, None] - C[None]) ** 2).sum(-1)
    z = d.argmin(1)
    frames.append((z.copy(), C.copy()))
    C = np.array([X[z == j].mean(0) for j in range(k)])

cols = ["#1F3A68", "#8A4B08", "#1E5E3A"]
fig, axes = plt.subplots(1, 4, figsize=(10.6, 2.8), sharey=True)
for ax, (z, cc), ttl in zip(axes, frames,
                            ["init centroids", "step 1", "step 2",
                             "converged"]):
    for j in range(k):
        ax.scatter(X[z == j, 0], X[z == j, 1], s=9, c=cols[j], alpha=0.7)
        ax.scatter(*cc[j], c=cols[j], marker="*", s=240,
                   edgecolor="k", linewidth=0.7, zorder=5)
    ax.set_title(ttl, fontsize=9)
    ax.set_xlabel("$x_1$")
axes[0].set_ylabel("$x_2$")
fig.tight_layout()
fig.savefig("figures/ch06/lloyd_steps.pdf")
print("wrote figures/ch06/lloyd_steps.pdf")
