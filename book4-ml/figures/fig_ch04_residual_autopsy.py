# figures/fig_ch04_residual_autopsy.py -- residuals raw vs log target.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

X, y = fetch_california_housing(return_X_y=True)
rng = np.random.default_rng(0)
idx = rng.choice(len(y), 4000, replace=False)
X, y = X[idx], y[idx]

fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4))
for ax, yt, lab in [(axes[0], y, "raw price"),
                    (axes[1], np.log1p(y), "log(1+price)")]:
    m = LinearRegression().fit(X, yt)
    r = yt - m.predict(X)
    ax.scatter(m.predict(X), r, s=4, alpha=0.35, color="#1F3A68")
    ax.axhline(0, color="k", lw=0.7)
    ax.set_xlabel("fitted value"); ax.set_ylabel("residual")
    ax.set_title(f"residuals vs fit --- {lab}  ($R^2={m.score(X,yt):.3f}$)")
axes[0].annotate("fan shape: error grows\nwith price -> heteroscedastic",
                 xy=(2.6, 3.4), fontsize=8, color="#8A4B08")
axes[1].annotate("log-target tightens\nthe funnel", xy=(0.6, 1.6),
                 fontsize=8, color="#1E5E3A")
fig.tight_layout()
fig.savefig("figures/ch04/residual_autopsy.pdf")
print("wrote figures/ch04/residual_autopsy.pdf")
