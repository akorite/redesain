# figures/fig_ch02_simpsons.py -- Simpson's paradox bar panel.
# Output: figures/ch02/simpsons.pdf
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("figures/ch02", exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False})

groups = ["History", "Computer Sci.", "POOLED"]
men = np.array([80.0, 20.0, 68.0])
women = np.array([85.0, 24.0, 34.2])

fig, ax = plt.subplots(figsize=(5.4, 2.9))
x = np.arange(3)
w = 0.34
b1 = ax.bar(x - w / 2, men, w, color="#1F3A68", label="men")
b2 = ax.bar(x + w / 2, women, w, color="#8A4B08", label="women")
for b in list(b1) + list(b2):
    ax.annotate(f"{b.get_height():.1f}%", (b.get_x() + b.get_width() / 2,
                b.get_height() + 1.5), ha="center", fontsize=7.5)
ax.set_xticks(x, groups)
ax.set_ylabel("admission rate")
ax.set_ylim(0, 100)
ax.axvspan(1.66, 2.4, color="#8A4B08", alpha=0.06)
ax.annotate("the pooled bars\nreverse both trends", (2.03, 74),
            ha="center", fontsize=8, color="#8A4B08")
ax.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1, 1))
fig.tight_layout()
fig.savefig("figures/ch02/simpsons.pdf")
print("wrote figures/ch02/simpsons.pdf")
