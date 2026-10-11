# figures/fig_ch04_sigmoid_boundary.py -- sigmoid + 2-D decision boundary.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
X = X[:, [23, 2]]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                    random_state=7, stratify=y)
mu, sd = Xtr.mean(0), Xtr.std(0)
Xtr, Xte = (Xtr - mu) / sd, (Xte - mu) / sd
w = np.array([-6.864, 0.608, -0.393])   # fitted by logreg_scratch.py

fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4))
z = np.linspace(-8, 8, 300)
axes[0].plot(z, 1 / (1 + np.exp(-z)), color="#1F3A68", lw=1.8)
axes[0].axvline(0, color="k", ls="--", lw=0.8)
axes[0].axhline(0.5, color="grey", ls=":", lw=0.8)
axes[0].set_xlabel("$\\mathbf{w}^T\\mathbf{x} + b$")
axes[0].set_ylabel("$\\sigma(\\cdot)$")
axes[0].set_title("the sigmoid turns a score into a probability")
xx, yy = np.meshgrid(np.linspace(Xtr[:,0].min()-0.4, Xtr[:,0].max()+0.4, 240),
                     np.linspace(Xtr[:,1].min()-0.4, Xtr[:,1].max()+0.4, 240))
G = np.c_[xx.ravel(), yy.ravel(), np.ones(xx.size)]
P = (1 / (1 + np.exp(-G @ w))).reshape(xx.shape)
ax = axes[1]
ax.contourf(xx, yy, P, levels=[0, 0.5, 1], colors=["#f5e0d8", "#dbe6f5"],
            alpha=0.9)
ax.contour(xx, yy, P, levels=[0.5], colors="k", linewidths=1.0)
ax.scatter(Xtr[ytr==0,0], Xtr[ytr==0,1], s=12, c="#8A4B08", marker="s",
           label="malignant")
ax.scatter(Xtr[ytr==1,0], Xtr[ytr==1,1], s=12, c="#1F3A68",
           label="benign")
ax.set_xlabel("worst radius (std)"); ax.set_ylabel("mean perimeter (std)")
ax.set_title("linear boundary, $p=0.5$ contour")
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig("figures/ch04/sigmoid_boundary.pdf")
print("wrote figures/ch04/sigmoid_boundary.pdf")
