import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(0,4,200);f=lambda t:(t-1.5)**3 - .4*(t-1.5)+1
fig,ax=plt.subplots(figsize=(5.2,2.7))
ax.plot(x,f(x),'k-',lw=1.8)
x0=1.8
ax.plot(x0,f(x0),'ko');x1=2.9
ax.plot([x0,x1],[f(x0),f(x0)+(x1-x0)*(f(x0+.05)-f(x0-.05))/.1],'r--',lw=1.5,
        label='analytic slope')
ax.plot([x0-.7,x0+.7],[f(x0-.7),f(x0+.7)],'b-.',lw=1.3,label=r'$(f{+}\epsilon)-(f{-}\epsilon)$')
ax.legend(fontsize=8);ax.set_xticks([]);ax.set_yticks([])
ax.set_xlabel(r"$\theta$ (one weight)");ax.set_ylabel("loss")
fig.tight_layout();fig.savefig('ch07/gradcheck.pdf')
