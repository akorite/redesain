# figures/fig_ch01_missing_scatter.py -> figures/ch01/missing_scatter.pdf
# Two panels: raw data with missing + injected-impossible values flagged,
# then the same scatter after cleaning. Run from repo root via `make figures`.
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

os.makedirs("figures/ch01", exist_ok=True)
plt.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.titlesize": 9.5,
    "axes.labelsize": 9, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "legend.fontsize": 8, "axes.spines.top": False, "axes.spines.right": False,
})

with open("data/penguins.csv", newline="") as f:
    rows = list(csv.reader(f))
header, data = rows[0], rows[1:]
ji = {h: i for i, h in enumerate(header)}

def col(name):
    return np.array([float(r[ji[name]]) if r[ji[name]] != "" else np.nan
                     for r in data])

bl, bd = col("bill_length_mm"), col("bill_depth_mm")
species = np.array([r[ji["species"]] for r in data])

# inject impossible values for the figure's hygiene demo (flagged, not hidden)
rng = np.random.default_rng(4)
bl_inj = bl.copy()
bad_i = rng.choice(np.where(~np.isnan(bl))[0], 3, replace=False)
bl_inj[bad_i] = [-2.0, 97.5, 62.0]          # impossible bill lengths (mm)
n_nan = np.isnan(bl).sum()

COLORS = {"Adelie": "#1F3A68", "Chinstrap": "#8A4B08", "Gentoo": "#1E5E3A"}
MARK = {"Adelie": "o", "Chinstrap": "s", "Gentoo": "^"}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.9), sharey=True)

# --- panel 1: as loaded (one impossible value stretches the axis) ---
for sp in COLORS:
    m = (species == sp) & ~np.isnan(bl) & ~np.isnan(bd)
    ax1.scatter(bl_inj[m], bd[m], s=9, c=COLORS[sp], marker=MARK[sp],
                alpha=0.55, lw=0, label=sp)
ax1.scatter(bl_inj[bad_i], bd[bad_i], s=55, marker="x", c="#B00020",
            lw=1.6, zorder=5, label="impossible value")
ax1.annotate(f"{n_nan} rows lack bill_length + bill_depth\n(cannot be drawn at all)",
             xy=(0.03, 0.06), xycoords="axes fraction", color="#B00020",
             fontsize=7.5)
ax1.set_title("as loaded: missing + impossible")
ax1.set_xlabel("bill length (mm)")
ax1.set_ylabel("bill depth (mm)")
ax1.legend(frameon=False, loc="upper right", markerscale=1.4)

# --- panel 2: after cleaning, the view snaps to the data ---
keep = ~np.isnan(bl) & ~np.isnan(bd) & (bl_inj > 10) & (bl_inj < 70)
for sp in COLORS:
    m = keep & (species == sp)
    ax2.scatter(bl[m], bd[m], s=9, c=COLORS[sp], marker=MARK[sp],
                alpha=0.55, lw=0)
ax2.set_title(f"after checks: {keep.sum()} rows kept")
ax2.set_xlabel("bill length (mm)")
ax2.set_xlim(30, 68)

fig.tight_layout()
fig.savefig("figures/ch01/missing_scatter.pdf")
print("wrote figures/ch01/missing_scatter.pdf  kept", int(keep.sum()),
      "of", len(bl))
