# code/ch05/tree_scratch.py -- a decision tree grown split by split.
# Gini criterion, best-of-all-thresholds split, depth cap, leaf majority.
# Run from the repository root:  python3 code/ch05/tree_scratch.py
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
names = load_wine().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)

def gini(labels):
    _, cnt = np.unique(labels, return_counts=True)
    p = cnt / len(labels)
    return 1 - (p ** 2).sum()

def best_split(X, y):
    base = gini(y); best = (-1, None, None)
    for j in range(X.shape[1]):
        for t in np.unique(X[:, j]):
            L, R = X[:, j] <= t, X[:, j] > t
            if L.sum() == 0 or R.sum() == 0:
                continue
            w = (L.sum() * gini(y[L]) + R.sum() * gini(y[R])) / len(y)
            gain = base - w
            if gain > best[0]:
                best = (gain, j, t)
    return best

def grow(X, y, depth, max_depth=3):
    if len(np.unique(y)) == 1 or depth == max_depth:
        vals, cnt = np.unique(y, return_counts=True)
        return ("leaf", vals[cnt.argmax()], len(y))
    gain, j, t = best_split(X, y)
    if gain <= 0:
        vals, cnt = np.unique(y, return_counts=True)
        return ("leaf", vals[cnt.argmax()], len(y))
    L = X[:, j] <= t
    return ("node", j, t, gain,
            grow(X[L], y[L], depth + 1, max_depth),
            grow(X[~L], y[~L], depth + 1, max_depth))

def show(node, ind=""):
    if node[0] == "leaf":
        print(f"{ind}predict class {node[1]} (n={node[2]})")
        return
    _, j, t, g, l, r = node
    print(f"{ind}if {names[j]} <= {t:.3f}   (gain {g:.4f})")
    show(l, ind + "  ")
    print(f"{ind}else")
    show(r, ind + "  ")

tree = grow(Xtr, ytr, 0)
show(tree)

def predict(node, x):
    while node[0] == "node":
        node = node[4] if x[node[1]] <= node[2] else node[5]
    return node[1]

pred = np.array([predict(tree, x) for x in Xte])
print(f"\ndepth-3 scratch tree: train acc "
      f"{(np.array([predict(tree,x) for x in Xtr]) == ytr).mean():.3f}  "
      f"test acc {(pred == yte).mean():.3f}")
