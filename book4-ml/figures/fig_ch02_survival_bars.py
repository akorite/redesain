# figures/fig_ch02_survival_bars.py -- grouped survival bars from the
# titanic groupby table. Output: figures/ch02/survival_bars.pdf
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

os.makedirs("figures/ch02", exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False})

df = pd.read_csv("data/titanic.csv")
wide = df.pivot_table(index="class", columns="sex", values="survived",
                      aggfunc="mean", observed=True) * 100
counts = df.groupby(["class", "sex"], observed=True)["survived"].count()

fig, ax = plt.subplots(figsize=(4.6, 2.9))
x = np.arange(len(wide.index))
w = 0.34
for k, sex in enumerate(["female", "male"]):
    vals = wide[sex].values
    bars = ax.bar(x + (k - 0.5) * w, vals, w,
                  color=["#8A4B08", "#1F3A68"][k], label=sex)
    for cls, b in zip(wide.index, bars):
        n = counts[(cls, sex)]
        ax.annotate(f"{b.get_height():.0f}%\n(n={n})",
                    (b.get_x() + w / 2, b.get_height() + 1.5),
                    ha="center", fontsize=7)
ax.set_xticks(x, wide.index)
ax.set_ylabel("survival rate (%)")
ax.set_ylim(0, 115)
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("figures/ch02/survival_bars.pdf")
print("wrote figures/ch02/survival_bars.pdf")
