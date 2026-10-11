# figures/fig_ch06_recon_strip.py -- digit rebuilt from k components.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
Xc = X - X.mean(0)
Vt = np.linalg.svd(Xc, full_matrices=False)[2]
i = 179
ks = [10, 30, 60]
fig, axes = plt.subplots(1, len(ks) + 1, figsize=(7.6, 2.2))
for ax, kk, ttl in [(axes[0], None, "original")] + \
                   list(zip(axes[1:], ks, [f"$k={k}$" for k in ks])):
    img = X[i] if kk is None else \
        X.mean(0) + (Xc[i] @ Vt[:kk].T) @ Vt[:kk]
    ax.imshow(img.reshape(8, 8), cmap="gray_r", vmin=0, vmax=16)
    ax.set_title(ttl, fontsize=9); ax.axis("off")
fig.suptitle("one `8' rebuilt from the top-$k$ SVD components", fontsize=10)
fig.tight_layout()
fig.savefig("figures/ch06/recon_strip.pdf")
print("wrote figures/ch06/recon_strip.pdf")
