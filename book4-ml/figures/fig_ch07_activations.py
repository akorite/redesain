import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
z = np.linspace(-4,4,400)
def sig(z): return 1/(1+np.exp(-z))
acts = [("sigmoid", sig(z), sig(z)*(1-sig(z))),
        ("tanh", np.tanh(z), 1-np.tanh(z)**2),
        ("ReLU", np.maximum(0,z), (z>0).astype(float)),
        ("leaky ReLU", np.where(z>0,z,.1*z), np.where(z>0,1,.1))]
fig,axes = plt.subplots(1,4,figsize=(10.5,2.3),sharex=True)
for ax,(nm,f,g) in zip(axes,acts):
    ax.plot(z,f,'k-',lw=1.6,label=nm); ax.plot(z,g,'r--',lw=1.1,label="gradient")
    ax.set_title(nm,fontsize=9); ax.set_ylim(-.4,1.6)
    ax.grid(alpha=.3); ax.legend(fontsize=6,loc='upper left')
axes[0].set_ylabel("value")
fig.tight_layout(); fig.savefig("ch07/activations.pdf")
