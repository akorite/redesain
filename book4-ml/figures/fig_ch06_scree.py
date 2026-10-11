# figures/fig_ch06_scree.py -- PCA scree + cumulative variance on digits.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
Xc = X - X.mean(0)
S = np.linalg.svd(Xc, full_matrices=False)[1]
share = (S ** 2 / (len(Xc) - 1)); share /= share.sum()
cum = np.cumsum(share)
k = np.arange(1, 65)

fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.bar(k, share * 100, color="#1F3A68", alpha=0.75, label="per component")
ax2 = ax.twinx()
ax2.plot(k, cum * 100, color="#8A4B08", lw=1.8, label="cumulative")
for t in [0.5, 0.9]:
    n = int(np.searchsorted(cum, t)) + 1
    ax2.axhline(t * 100, color="grey", ls=":", lw=0.7)
    ax2.annotate(f"{int(t*100)}% at $k={n}$", xy=(n, t * 100),
                 xytext=(n + 6, t * 100 - 7), fontsize=8,
                 arrowprops=dict(arrowstyle="->", lw=0.7))
ax.set_xlabel("component"); ax.set_ylabel("variance share (%)")
ax2.set_ylabel("cumulative (%)"); ax2.set_ylim(0, 105)
fig.tight_layout()
fig.savefig("figures/ch06/scree.pdf")
print("wrote figures/ch06/scree.pdf")
