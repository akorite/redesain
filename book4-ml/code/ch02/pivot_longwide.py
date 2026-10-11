# code/ch02/pivot_longwide.py -- long <-> wide reshaping on real data.
# Run from the repository root:  python3 code/ch02/pivot_longwide.py
import pandas as pd

fl = pd.read_csv("data/flights.csv")
print("long shape:", fl.shape)
print(fl.head(3).to_string(index=False), "\n")

# long -> wide: one row per year, one column per month
wide = fl.pivot(index="year", columns="month", values="passengers")
print("wide shape:", wide.shape)
print(wide.head(4).to_string())
print("\nrow index:", wide.index.name, "| col index:", wide.columns.name)

# wide -> long: melt is the inverse
back = wide.melt(ignore_index=False).reset_index()
print("\nback to long, sorted:")
back = back.sort_values(["year", "month"], ignore_index=True)
print(back.head(3).to_string(index=False))
print("matches original (set-compare):",
      set(map(tuple, back[["year", "month", "value"]].values))
      == set(map(tuple, fl.values)))
