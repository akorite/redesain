# figures/fig_ch04_lambda_ucurve.py -- train/test MSE vs lambda.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=7)
n, d = Xtr.shape
Xb = np.c_[Xtr, np.ones(n)]; Xte_b = np.c_[Xte, np.ones(len(Xte))]
lams = np.logspace(-4, 4, 60)
tr_mse, te_mse = [], []
for lam in lams:
    I = np.eye(d + 1); I[-1, -1] = 0
    th = np.linalg.solve(Xb.T @ Xb + lam * I, Xb.T @ ytr)
    tr_mse.append(((Xb @ th - ytr) ** 2).mean())
    te_mse.append(((Xte_b @ th - yte) ** 2).mean())

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.semilogx(lams, tr_mse, "o-", ms=3, color="#8A4B08", label="train MSE")
ax.semilogx(lams, te_mse, "s-", ms=3, color="#1F3A68", label="test MSE")
best = lams[int(np.argmin(te_mse))]
ax.axvline(best, color="k", ls="--", lw=0.8)
ax.annotate(f"test minimum at $\\lambda\\approx{best:.2f}$",
            xy=(best, min(te_mse)), xytext=(best*30, min(te_mse)+500),
            fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
ax.set_xlabel("$\\lambda$"); ax.set_ylabel("MSE")
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("figures/ch04/lambda_ucurve.pdf")
print("wrote figures/ch04/lambda_ucurve.pdf")
