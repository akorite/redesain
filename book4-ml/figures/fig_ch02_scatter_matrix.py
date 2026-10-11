# figures/fig_ch02_scatter_matrix.py -- scatter matrix of the four numeric
# penguin columns, coloured by species. Output: figures/ch02/scatter_matrix.pdf
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("figures/ch02", exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 8})

df = pd.read_csv("data/penguins.csv")
cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
short = ["bill len.", "bill dep.", "flipper", "mass"]
spec = {"Adelie": ("#1F3A68", "o"), "Chinstrap": ("#8A4B08", "s"),
        "Gentoo": ("#1E5E3A", "^")}

fig, axes = plt.subplots(4, 4, figsize=(6.4, 6.4), sharex="col", sharey="row")
for i, yi in enumerate(cols):
    for j, xi in enumerate(cols):
        ax = axes[i, j]
        if i == j:
            ax.hist([df.loc[df.species == s, yi].dropna() for s in spec],
                    bins=12, color=[spec[s][0] for s in spec], alpha=0.85)
        else:
            for s, (c, m) in spec.items():
                ax.plot(df.loc[df.species == s, xi],
                        df.loc[df.species == s, yi],
                        m, ms=2.5, color=c, alpha=0.7, mew=0)
        if i == 3:
            ax.set_xlabel(short[j])
        if j == 0:
            ax.set_ylabel(short[i])
        ax.tick_params(labelsize=6)
handles = [plt.Line2D([], [], marker=m, color=c, ls="", ms=5, label=s)
           for s, (c, m) in spec.items()]
fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False,
           fontsize=8, bbox_to_anchor=(0.5, 1.02))
fig.tight_layout(rect=[0, 0, 1, 0.98])
fig.savefig("figures/ch02/scatter_matrix.pdf")
print("wrote figures/ch02/scatter_matrix.pdf")
