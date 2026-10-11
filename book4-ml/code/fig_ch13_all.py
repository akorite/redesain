# fig_ch13_all.py -- all ch13 compiled figures, from real saved arrays.
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
M = dict(fontsize=7)
res = np.load('/tmp/bandit_curves.npy', allow_pickle=True).item()
fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.6))
for name, (r, o) in res.items():
    axes[0].plot(np.convolve(r, np.ones(50)/50, 'same'), label=name)
    axes[1].plot(np.convolve(o, np.ones(50)/50, 'same'), label=name)
axes[0].set_title('mean reward per step (2000-run average)', **M)
axes[1].set_title('fraction optimal action', **M)
axes[1].legend(fontsize=5); [a.grid(alpha=.3) for a in axes]
fig.tight_layout(); fig.savefig('ch13/bandit_curves.pdf'); plt.close(fig)
Q = np.load('/tmp/qlearn_Q.npy'); V = Q.max(2); pol = Q.argmax(2)
HOLES = {(1,1),(1,3),(2,3),(3,0)}
arrows = {0:(-0.3,0),1:(0,-0.3),2:(0.3,0),3:(0,0.3)}
fig, ax = plt.subplots(figsize=(3.4,3.2))
ax.imshow(V, cmap='viridis')
for r in range(4):
    for c in range(4):
        s=(r,c)
        if s==(3,3): ax.text(c,r,'G',ha='center',va='center',fontsize=11,color='w')
        elif s in HOLES: ax.text(c,r,'X',ha='center',va='center',fontsize=11,color='w')
        else:
            dx,dy = arrows[pol[r,c]]
            ax.arrow(c-dx*0.6,r-dy*0.6,dx*1.2,dy*1.2,head_width=0.12,color='w')
            ax.text(c,r,f'{V[r,c]:.2f}',ha='center',va='center',fontsize=5,color='k')
ax.set_xticks(range(4));ax.set_yticks(range(4))
ax.set_title('V*(s) heat + greedy policy (real Q-table)', **M)
fig.tight_layout(); fig.savefig('ch13/gridworld_policy.pdf'); plt.close(fig)
rews = np.load('/tmp/qlearn_rews.npy')
fig, ax = plt.subplots(figsize=(4.2,2.3))
ax.plot(np.convolve(rews, np.ones(20)/20, 'same'), 'b-')
ax.axhline(0.93, color='r', ls='--', lw=0.8); ax.text(400, 0.4, 'ep799 return 0.93', **M)
ax.set_xlabel('episode'); ax.set_ylabel('return'); ax.grid(alpha=.3)
ax.set_title('Q-learning on the 4x4 lake: -1.45 -> 0.93 (real)', **M)
fig.tight_layout(); fig.savefig('ch13/qlearn_curve.pdf'); plt.close(fig)
lens = np.load('/tmp/cartpole_lens.npy')
fig, ax = plt.subplots(figsize=(4.2,2.3))
ax.plot(np.convolve(lens, np.ones(15)/15, 'same'), 'b-')
ax.axhline(200, color='r', ls='--', lw=0.8)
ax.set_xlabel('episode'); ax.set_ylabel('steps survived'); ax.grid(alpha=.3)
ax.set_title('linear-Q CartPole: learns, then unlearns (real run)', **M)
fig.tight_layout(); fig.savefig('ch13/cartpole_fail.pdf'); plt.close(fig)
print('figs done')
