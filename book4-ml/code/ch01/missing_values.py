# code/ch01/missing_values.py -- find NaNs, then measure what each fix costs.
# Run from the repository root:  python3 code/ch01/missing_values.py
import csv
import numpy as np

NUMERIC = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

with open("data/penguins.csv", newline="") as f:
    rows = list(csv.reader(f))
header, data = rows[0], rows[1:]
ji = {h: i for i, h in enumerate(header)}

print("missing cells per column:")
for h in header:
    n_miss = sum(1 for r in data if r[ji[h]] == "")
    if n_miss:
        print(f"  {h:<18}{n_miss}")

X = np.array([[float(r[ji[c]]) if r[ji[c]] != "" else np.nan for c in NUMERIC]
              for r in data])
bad_rows = np.isnan(X).any(axis=1)
print(f"\nrows with >=1 missing numeric: {bad_rows.sum()} of {len(X)}")

# strategy 1: drop the rows
X_drop = X[~bad_rows]
# strategy 2: fill each column with its observed median
med = np.nanmedian(X, axis=0)
X_fill = np.where(bad_rows[:, None], med[None, :], X)

print("column means  drop-rows vs fill-median:")
for j, h in enumerate(NUMERIC):
    print(f"  {h:<18}{X_drop[:, j].mean():8.2f}   {X_fill[:, j].mean():8.2f}")
print("corr(bill_length, body_mass)  drop / fill:",
      f"{np.corrcoef(X_drop[:, 0], X_drop[:, 3])[0, 1]:.3f} /",
      f"{np.corrcoef(X_fill[:, 0], X_fill[:, 3])[0, 1]:.3f}")
