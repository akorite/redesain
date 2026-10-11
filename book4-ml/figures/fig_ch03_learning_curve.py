# figures/fig_ch03_learning_curve.py -- accuracy vs train size, NB vs kNN.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

X, y = load_digits(return_X_y=True)
rng = np.random.default_rng(2)
perm = rng.permutation(len(y)); te = perm[:400]; pool = perm[400:]
sizes = [30, 60, 120, 240, 500, 900, 1397]
nb_acc, knn_acc = [], []
for n in sizes:
    tr = pool[:n]
    nb_acc.append(GaussianNB().fit(X[tr], y[tr]).score(X[te], y[te]))
    knn_acc.append(KNeighborsClassifier(5).fit(X[tr], y[tr]).score(X[te], y[te]))

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.semilogx(sizes, nb_acc, "o-", color="#8A4B08", label="Gaussian NB")
ax.semilogx(sizes, knn_acc, "s-", color="#1F3A68", label="kNN ($k=5$)")
ax.set_xlabel("training-set size $n$")
ax.set_ylabel("test accuracy")
ax.legend(fontsize=8, loc="lower right")
ax.annotate("more data helps the\nflexible model more", xy=(900, 0.95),
            xytext=(60, 0.93), fontsize=8,
            arrowprops=dict(arrowstyle="->", lw=0.8))
fig.tight_layout()
fig.savefig("figures/ch03/learning_curve.pdf")
print("wrote figures/ch03/learning_curve.pdf")
