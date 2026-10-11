# code/ch01/duplicates_leak.py -- how a duplicated row inflates test accuracy.
# Run from the repository root:  python3 code/ch01/duplicates_leak.py
import csv
import numpy as np

with open("data/iris.csv", newline="") as f:
    rows = list(csv.reader(f))[1:]
X = np.array([[float(v) for v in r[:4]] for r in rows])
y = np.array([r[4] for r in rows])

def knn1(Xtr, ytr, Xte):
    """1-nearest-neighbour: the cheapest memoriser (ch3 formalises it)."""
    d2 = ((Xte[:, None, :] - Xtr[None, :, :]) ** 2).sum(-1)
    return ytr[d2.argmin(1)]

def split_accuracy(X, y, seed):
    rng = np.random.default_rng(seed)
    perm = rng.permutation(len(y))
    k = int(0.8 * len(y))
    tr, te = perm[:k], perm[k:]
    return (knn1(X[tr], y[tr], X[te]) == y[te]).mean()

# plant 40 duplicate rows across classes (a scraped dataset often has this)
rng = np.random.default_rng(1)
pick = rng.choice(len(X), size=40, replace=False)
Xd = np.vstack([X, X[pick]])
yd = np.concatenate([y, y[pick]])

# shuffle-then-split WITHOUT deduplication: twins land on both sides of the split
leak = np.mean([split_accuracy(Xd, yd, s) for s in range(10)])

# deduplicate FIRST, then split: no row can appear on both sides
Xu, iu = np.unique(Xd, axis=0, return_index=True)
yu = yd[iu]
honest = np.mean([split_accuracy(Xu, yu, s) for s in range(10)])

print(f"dataset: {len(X)} rows -> {len(Xd)} after planting 40 duplicate rows")
print(f"split-then-eval, duplicates in:    {leak:.3f} mean test acc (10 seeds)")
print(f"dedup first, then split and eval:  {honest:.3f} mean test acc (10 seeds)")
print(f"phantom gain: {(leak - honest) * 100:+.1f} percentage points")

# the same bug on a harder task: two overlapping blobs, 1-NN base acc ~0.85
def blobs(n, seed):
    r = np.random.default_rng(seed)
    Xa = r.normal([0, 0], 1.4, (n // 2, 2))
    Xb = r.normal([1.6, 0.4], 1.4, (n - n // 2, 2))
    return np.vstack([Xa, Xb]), np.array([0] * (n // 2) + [1] * (n - n // 2))

Xs, ys = blobs(500, 3)
pick = rng.choice(len(Xs), size=150, replace=False)
Xsd, ysd = np.vstack([Xs, Xs[pick]]), np.concatenate([ys, ys[pick]])
leak_s = np.mean([split_accuracy(Xsd, ysd, s) for s in range(10)])
Xsu, iu = np.unique(Xsd, axis=0, return_index=True)
honest_s = np.mean([split_accuracy(Xsu, ysd[iu], s) for s in range(10)])
print(f"\nblobs: {len(Xs)} rows -> {len(Xsd)} with 150 planted duplicates")
print(f"split-then-eval, duplicates in:    {leak_s:.3f} mean test acc (10 seeds)")
print(f"dedup first, then split and eval:  {honest_s:.3f} mean test acc (10 seeds)")
print(f"phantom gain: {(leak_s - honest_s) * 100:+.1f} percentage points")

# emit the bar-chart data the chapter figure reads (figures/ch01/leak.dat)
import os
os.makedirs("figures/ch01", exist_ok=True)
with open("figures/ch01/leak.dat", "w") as f:
    f.write("scenario leak honest gain\n")
    f.write(f"iris {leak:.3f} {honest:.3f} {(leak - honest) * 100:.1f}\n")
    f.write(f"blobs {leak_s:.3f} {honest_s:.3f} {(leak_s - honest_s) * 100:.1f}\n")
