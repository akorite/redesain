# code/ch02/penguins_corr_flip.py -- a real correlation reversal hiding
# inside the penguins table. Run:  python3 code/ch02/penguins_corr_flip.py
import pandas as pd

df = pd.read_csv("data/penguins.csv")
cols = ["bill_length_mm", "bill_depth_mm"]

print("pooled correlation (342 complete pairs):")
print(f"  all species together: r = {df[cols].corr().iloc[0, 1]:+.3f}")

print("\nper species:")
for s, g in df.groupby("species"):
    r = g[cols].corr().iloc[0, 1]
    print(f"  {s:<9} (n={len(g):3d}): r = {r:+.3f}")

print("\nsame table, three opposite stories -- the aggregate lied.")
