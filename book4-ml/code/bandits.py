# bandits.py -- the 10-armed testbed, S&B style: eps-greedy vs UCB vs
# optimistic-init, mean reward + %optimal-action over 2000 runs x 1000 steps.
import numpy as np

rng = np.random.default_rng(0)
K, RUNS, STEPS = 10, 2000, 1000
qstar_all = rng.normal(0., 1., (RUNS, K))          # true means per run
optimal = qstar_all.argmax(1)

def play(kind, eps=0.1, c=2.0, q0=0.0):
    """returns (mean reward per step, frac optimal action per step)."""
    Q = np.full((RUNS, K), q0)
    N = np.zeros((RUNS, K))
    rew = np.zeros(STEPS); opt = np.zeros(STEPS)
    for t in range(STEPS):
        u = rng.random(RUNS)
        if kind == 'greedy':
            a = Q.argmax(1)
        elif kind == 'eps':
            a = np.where(u < eps, rng.integers(0, K, RUNS), Q.argmax(1))
        elif kind == 'ucb':
            a = (Q + c * np.sqrt(np.log(t + 1) / (N + 1e-9))).argmax(1)
        elif kind == 'optimistic':
            a = np.where(u < eps, rng.integers(0, K, RUNS), Q.argmax(1))
        r = rng.normal(qstar_all[np.arange(RUNS), a], 1.)
        N[np.arange(RUNS), a] += 1
        Q[np.arange(RUNS), a] += (r - Q[np.arange(RUNS), a]) / N[np.arange(RUNS), a]
        rew[t] = r.mean(); opt[t] = (a == optimal).mean()
    return rew, opt

results = {}
for name, kw in [('greedy', dict(kind='greedy')),
                 ('eps-greedy .1', dict(kind='eps')),
                 ('UCB c=2', dict(kind='ucb')),
                 ('optimistic Q0=5', dict(kind='optimistic', eps=0.0, q0=5.0))]:
    results[name] = play(**kw)
    r, o = results[name]
    print(f"{name:16s} mean-reward(1000)={r[-1]:.3f}  "
          f"%optimal(last100)={o[-100:].mean()*100:.0f}%")

np.save('/tmp/bandit_curves.npy',
        {k: v for k, v in results.items()}, allow_pickle=True)
print("saved /tmp/bandit_curves.npy")
