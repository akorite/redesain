# code/ch01/onehot_scratch.py -- one-hot encode categorical columns, from scratch.
# Run from the repository root:  python3 code/ch01/onehot_scratch.py
import csv
import numpy as np

def load_columns(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]

def onehot_column(values):
    """Return (block, names): (n, k) 0/1 float block, one column per observed level
    plus an extra column for missing entries ('')."""
    levels = sorted({v for v in values if v != ""})
    names = levels + (["<missing>"] if "" in values else [])
    idx = {v: i for i, v in enumerate(levels)}
    B = np.zeros((len(values), len(names)))
    for i, v in enumerate(values):
        B[i, idx[v] if v != "" else len(levels)] = 1.0
    return B, names

header, data = load_columns("data/penguins.csv")
num_cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
cat_cols = ["sex", "island"]
ji = {h: i for i, h in enumerate(header)}

# numeric block: empty -> NaN  (float array can hold NaN)
Xnum = np.array([[float(r[ji[c]]) if r[ji[c]] != "" else np.nan
                  for c in num_cols] for r in data])
blocks, names = [Xnum], list(num_cols)
for c in cat_cols:
    B, bn = onehot_column([r[ji[c]] for r in data])
    blocks.append(B)
    names += [f"{c}={n}" for n in bn]

X = np.concatenate(blocks, axis=1)
print("numeric cols:", len(num_cols), " categorical cols:", cat_cols)
print("one-hot names:", names[len(num_cols):])
print(f"shape change: ({len(data)}, {len(num_cols) + len(cat_cols)}) -> {X.shape}")
print("first encoded row:", np.array2string(X[0], precision=1, separator=", ",
      suppress_small=True))
