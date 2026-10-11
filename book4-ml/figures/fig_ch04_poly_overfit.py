# figures/fig_ch04_poly_overfit.py -- degree 1/3/9 strip.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

rng = np.random.default_rng(4)
x = np.sort(rng.uniform(0, 1.2, 26))
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.25, len(x))
xx = np.linspace(0, 1.2, 300)

fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.0), sharey=True)
for ax, deg in zip(axes, [1, 3, 9]):
    m = make_pipeline(PolynomialFeatures(deg, include_bias=False),
                      LinearRegression()).fit(x[:, None], y)
    ax.plot(xx, np.sin(2 * np.pi * xx), "k--", lw=0.9, label="truth")
    ax.plot(xx, m.predict(xx[:, None]), color="#1F3A68", lw=1.6,
            label=f"deg {deg}")
    ax.scatter(x, y, s=14, c="#8A4B08", zorder=3)
    ax.set_title(f"degree {deg}")
    ax.set_xlabel("$x$"); ax.set_ylim(-2.2, 2.2)
    r2 = m.score(x[:, None], y)
    ax.text(0.05, -1.9, f"train $R^2={r2:.2f}$", fontsize=8)
axes[0].set_ylabel("$y$")
axes[0].legend(fontsize=8, loc="upper right")
fig.tight_layout()
fig.savefig("figures/ch04/poly_overfit.pdf")
print("wrote figures/ch04/poly_overfit.pdf")
