# code/ch03/eval_protocol.py -- the canonical split + metric harness,
# reused by every later chapter. Stratified 80/20, confusion-based metrics.
# Run from the repository root:  python3 code/ch03/eval_protocol.py
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = load_breast_cancer(return_X_y=True)   # y=1 benign, y=0 malignant
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=7, stratify=y)
print(f"split: {len(ytr)} train / {len(yte)} test "
      f"(positive rate {ytr.mean():.3f} both folds)")

model = LogisticRegression(max_iter=5000).fit(Xtr, ytr)
pred = model.predict(Xte)

def confusion(pred, y):
    tp = int(((pred == 1) & (y == 1)).sum())
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    tn = int(((pred == 0) & (y == 0)).sum())
    return tp, fp, fn, tn

tp, fp, fn, tn = confusion(pred, yte)
prec = tp / (tp + fp)
rec = tp / (tp + fn)
f1 = 2 * prec * rec / (prec + rec)
print(f"[[{tn:>3} {fp:>3}]")
print(f" [{fn:>3} {tp:>3}]]")
print(f"accuracy  {(pred == yte).mean():.3f}")
print(f"precision {prec:.3f}   (of predicted-positive, how many truly are)")
print(f"recall    {rec:.3f}   (of truly-positive, how many we caught)")
print(f"F1        {f1:.3f}")
# the imbalance lesson: predicting everyone 'benign' also scores high
lazy_acc = yte.mean()
print(f"\nlazy 'all benign' baseline accuracy: {lazy_acc:.3f}")
print("F1 is the honest metric here -- a cancer missed is not a tie.")
