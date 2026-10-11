# code/ch02/two_plots_one_truth.py -- the same data, one misleading plot,
# one honest one. Output: figures/ch02/two_plots.pdf  + printed deltas.
# Run from the repository root:  python3 code/ch02/two_plots_one_truth.py
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("figures/ch02", exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False})

fl = pd.read_csv("data/flights.csv")
yearly = fl.groupby("year")["passengers"].mean()
print("mean monthly passengers by year (1949-1951, 1959-1960):")
print(yearly.loc[[1949, 1950, 1951, 1959, 1960]].round(1).to_string())
print(f"\n1949 -> 1960 growth: {yearly[1960] / yearly[1949] - 1:.1%}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.8))
# left: the misleading one -- y starts at 100, growth looks explosive
ax1.plot(yearly.index, yearly.values, marker="o", ms=3, color="#8A4B08")
ax1.set_ylim(100, 500)
ax1.set_title("mean passengers by year\n(y-axis starts at 100)", fontsize=9.5)
ax1.set_xlabel("year")
# right: the honest one -- same data, axis includes zero
ax2.plot(yearly.index, yearly.values, marker="o", ms=3, color="#1F3A68")
ax2.set_ylim(0, 500)
ax2.set_title("same data, y-axis includes 0", fontsize=9.5)
ax2.set_xlabel("year")
fig.tight_layout()
fig.savefig("figures/ch02/two_plots.pdf")
print("wrote figures/ch02/two_plots.pdf")
