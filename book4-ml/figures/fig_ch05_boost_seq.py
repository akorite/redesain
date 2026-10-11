# figures/fig_ch05_boost_seq.py -- boosting stage-by-stage residual fits.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

rng = np.random.default_rng(5)
x = np.sort(rng.uniform(0, 1.2, 80))
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.3, len(x))
xx = np.linspace(0, 1.2, 400)
lr = 0.5
F = np.full(len(x), y.mean())
Fte = np.full(len(xx), y.mean())
fig, axes = plt.subplots(1, 4, figsize=(10.4, 2.9), sharey=True)
for i, ax in enumerate(axes):
    if i:
        t = DecisionTreeRegressor(max_depth=2, random_state=i)
        t.fit(x[:, None], y - F)
        F += lr * t.predict(x[:, None])
        Fte += lr * t.predict(xx[:, None])
    ax.scatter(x, y, s=11, c="#8A4B08", alpha=0.65)
    ax.plot(xx, Fte, color="#1F3A68", lw=1.8)
    ax.plot(xx, np.sin(2 * np.pi * xx), "k--", lw=0.9)
    ax.set_title(f"after stage {i}", fontsize=9)
    ax.set_xlabel("$x$")
axes[0].set_ylabel("$y$")
fig.suptitle("each stage fits the residuals of the current model", fontsize=10)
fig.tight_layout()
fig.savefig("figures/ch05/boost_seq.pdf")
print("wrote figures/ch05/boost_seq.pdf")
