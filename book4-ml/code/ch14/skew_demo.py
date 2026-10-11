# skew_demo.py -- train/serve skew made visible.
# We fit a classifier on standardised features; at serve time the
# normalisation is recomputed *per request* (the classic bug).
# Same model, same data -- metrics diverge.
import numpy as np
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

X, y = load_wine(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3,
                                    random_state=0, stratify=y)

# training path: scaler fit on TRAIN only, applied to both splits
scaler = StandardScaler().fit(Xtr)
clf = LogisticRegression(max_iter=5000)
clf.fit(scaler.transform(Xtr), ytr)
train_world_acc = accuracy_score(yte, clf.predict(scaler.transform(Xte)))
print(f"train-world accuracy (consistent scaler): {train_world_acc:.3f}")

# serve-time bug: a new scaler fit per incoming batch of test rows
bugged = np.concatenate([
    clf.predict(StandardScaler().fit_transform(batch.reshape(-1, 13)))
    for batch in np.array_split(Xte, 6)])
bugged_acc = accuracy_score(yte, bugged)
print(f"serve accuracy (per-batch re-fit scaler):  {bugged_acc:.3f}")

# the same bug one row at a time (realistic: requests arrive singly)
solo = np.array([clf.predict(StandardScaler().fit_transform(
    x.reshape(1, -1)))[0] for x in Xte])
solo_acc = accuracy_score(yte, solo)
print(f"serve accuracy (per-request re-fit):       {solo_acc:.3f}")
print(f"divergence train-vs-solo: {train_world_acc - solo_acc:+.3f}")
