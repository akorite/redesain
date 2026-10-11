# code/ch06/cluster_lib.py -- sklearn KMeans/Agglomerative + silhouette/ARI
# on digits, plus the clusters-in-noise trap.
# Run from the repository root:  python3 code/ch06/cluster_lib.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, adjusted_rand_score

X, y = load_digits(return_X_y=True)
print("digits (10 true digits):")
for name, z in [("KMeans k=10",
                 KMeans(10, n_init=10, random_state=7).fit_predict(X)),
                ("Agglomerative ward",
                 AgglomerativeClustering(10).fit_predict(X))]:
    print(f"  {name:>20}: ARI {adjusted_rand_score(y, z):.3f}  "
          f"silhouette {silhouette_score(X, z):.3f}")

print("\nk-sweep on iris (k-means silhouette):")
from sklearn.datasets import load_iris
Xi, yi = load_iris(return_X_y=True)
for k in [2, 3, 4]:
    z = KMeans(k, n_init=10, random_state=7).fit_predict(Xi)
    print(f"  k={k}: silhouette {silhouette_score(Xi, z):.3f}  "
          f"ARI-vs-species {adjusted_rand_score(yi, z):.3f}")

print("\nthe trap: k-means on pure uniform noise")
rng = np.random.default_rng(0)
N = rng.uniform(0, 1, (300, 8))
for k in [3, 5]:
    z = KMeans(k, n_init=10, random_state=7).fit_predict(N)
    print(f"  uniform data, k={k}: silhouette {silhouette_score(N, z):.3f}")
print("  non-trivial silhouette on *noise* -- the score measures cluster")
print("  shape, not cluster truth. Compare against a null baseline first.")
