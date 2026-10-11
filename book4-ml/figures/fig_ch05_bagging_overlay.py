# figures/fig_ch05_bagging_overlay.py -- 20 trees overlaid vs bagged mean.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

rng = np.random.default_rng(1)
x = np.sort(rng.uniform(0, 1, 60))
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.35, len(x))
xx = np.linspace(0, 1, 400)

fig, ax = plt.subplots(figsize=(6.2, 3.4))
preds = []
for b in range(20):
    bi = rng.choice(len(x), len(x), replace=True)
    m = DecisionTreeRegressor(random_state=b).fit(x[bi, None], y[bi])
    p = m.predict(xx[:, None]); preds.append(p)
    ax.plot(xx, p, color="#1F3A68", alpha=0.14, lw=0.8)
ax.plot(xx, np.mean(preds, axis=0), color="#1F3A68", lw=2.4,
        label="bagged mean of 20 trees")
ax.plot(xx, np.sin(2 * np.pi * xx), "k--", lw=1.2, label="truth")
ax.scatter(x, y, s=13, c="#8A4B08", zorder=5, label="data")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
ax.set_title("single trees disagree; their average does not")
ax.legend(fontsize=8, loc="lower left")
fig.tight_layout()
fig.savefig("figures/ch05/bagging_overlay.pdf")
print("wrote figures/ch05/bagging_overlay.pdf")
