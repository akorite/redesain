# figures/fig_ch04_coef_paths.py -- ridge vs lasso coefficient paths.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge, Lasso

X, y = load_diabetes(return_X_y=True)
names = load_diabetes().feature_names
lams = np.logspace(-3, 3, 60)
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4), sharey=True)
for ax, model, title in [(axes[0], Ridge, "ridge $\\|\\theta\\|_2^2$"),
                         (axes[1], Lasso, "lasso $\\|\\theta\\|_1$")]:
    paths = []
    for lam in lams:
        m = model(alpha=lam, max_iter=8000).fit(X, y)
        paths.append(m.coef_)
    paths = np.array(paths)
    for i, nm in enumerate(names):
        ax.semilogx(lams, paths[:, i], lw=1.1, label=nm)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel("$\\lambda$"); ax.set_title(title)
axes[0].set_ylabel("coefficient value")
axes[1].legend(fontsize=6.5, ncol=2, loc="upper right")
axes[0].annotate("all shrink smoothly,\nnone hit exactly 0", xy=(0.3, 300),
                 fontsize=8)
axes[1].annotate("corners of the L1 ball\nsend coefs to exact 0",
                 xy=(0.3, -700), fontsize=8)
fig.tight_layout()
fig.savefig("figures/ch04/coef_paths.pdf")
print("wrote figures/ch04/coef_paths.pdf")
