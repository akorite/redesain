# code/ch02/titanic_groupby.py -- survival rate by class x sex via groupby.
# Run from the repository root:  python3 code/ch02/titanic_groupby.py
import pandas as pd

df = pd.read_csv("data/titanic.csv")
print("shape:", df.shape)
print("dtypes (first 8):\n", df.dtypes.head(8), "\n")

# the SQL-shaped verb: SELECT class, sex, mean(survived), count(*) GROUP BY 1,2
rate = df.groupby(["class", "sex"], observed=True)["survived"].agg(["mean", "count"])
rate["mean"] = (rate["mean"] * 100).round(1)
rate.columns = ["survival_%", "n"]
print("survival rate by class x sex:")
print(rate)

# the same answer as a matrix (unstack = pivot one index level into columns)
print("\nas a wide table:")
wide = df.pivot_table(index="class", columns="sex", values="survived",
                      aggfunc="mean", observed=True)
print((wide * 100).round(1).astype(str) + " %")

# select-and-aggregate in one line, no groupby needed
print("\nFirst-class women aged <=16, survival:",
      df.query("sex == 'female' and `class` == 'First' and age <= 16")
        ["survived"].mean().round(3))
