# code/ch02/simpsons.py -- Simpson's paradox: the pooled rate reverses
# every per-group trend. Synthetic admissions table (Berkeley-style).
# Run from the repository root:  python3 code/ch02/simpsons.py
import pandas as pd

# admit, applied per department x sex. Women win BOTH departments, yet lose
# the pooled comparison because they apply mostly to the selective one.
rows = [
    ("History",        "men",   640, 800),   # 80% -- the easy department
    ("History",        "women",  85, 100),   # 85%
    ("Computer Sci.",  "men",    40, 200),   # 20% -- the selective one
    ("Computer Sci.",  "women", 120, 500),   # 24%
]
df = pd.DataFrame(rows, columns=["dept", "sex", "admitted", "applied"])
df["rate"] = df.admitted / df.applied

print("per department:")
print(df.pivot(index="dept", columns="sex", values="rate")
      .to_string(float_format=lambda v: f"{v:.1%}"))

pooled = df.groupby("sex")[["admitted", "applied"]].sum()
pooled["rate"] = pooled.admitted / pooled.applied
print("\npooled across departments:")
print(pooled.rate.to_string(float_format=lambda v: f"{v:.1%}"))

print(f"\nverdict: women beat men in BOTH departments "
      f"({df.rate[1]:.1%}>{df.rate[0]:.1%}, {df.rate[3]:.1%}>{df.rate[2]:.1%})",
      "yet lose the pooled comparison",
      f"({pooled.rate['women']:.1%} < {pooled.rate['men']:.1%})")
