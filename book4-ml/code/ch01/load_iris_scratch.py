# code/ch01/load_iris_scratch.py -- CSV -> ndarray with the csv module (no pandas).
# Run from the repository root:  python3 code/ch01/load_iris_scratch.py
import csv

def load_csv_xy(path, target_col):
    """Return (X, y, feature_names): X float ndarray, y string ndarray."""
    import numpy as np
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    header, data = rows[0], rows[1:]
    j = header.index(target_col)
    feature_names = [h for i, h in enumerate(header) if i != j]
    X = np.array([[float(v) for i, v in enumerate(r) if i != j] for r in data])
    y = np.array([r[j] for r in data])
    return X, y, feature_names

X, y, names = load_csv_xy("data/iris.csv", "species")
print("feature names:", names)
print("X.shape =", X.shape, " X.dtype =", X.dtype)
print("y.shape =", y.shape, " classes:", sorted(set(y.tolist())))

# --- distance-to-mean classifier on a seeded 80/20 split ---
import numpy as np
rng = np.random.default_rng(7)
perm = rng.permutation(len(y))
n_train = int(0.8 * len(y))
tr, te = perm[:n_train], perm[n_train:]
classes = np.unique(y)
cent = np.stack([X[tr][y[tr] == c].mean(axis=0) for c in classes])
pred = classes[((X[te][:, None, :] - cent[None, :, :]) ** 2).sum(-1).argmin(1)]
acc = (pred == y[te]).mean()
print(f"split: {len(tr)} train / {len(te)} test (seed 7)")
print(f"distance-to-mean test accuracy: {acc:.3f}  ({int((pred == y[te]).sum())}/{len(te)})")
