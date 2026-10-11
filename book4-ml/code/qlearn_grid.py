# qlearn_grid.py -- tabular Q-learning on a 4x4 FrozenLake-style grid:
# start (0,0), goal (3,3), holes at (1,1),(1,3),(2,3),(3,0).
# Actions: 0=L 1=D 2=R 3=U. Reward: +1 goal, -1 hole, -0.01 per step.
import numpy as np

rng = np.random.default_rng(0)
N = 4
HOLES = {(1, 1), (1, 3), (2, 3), (3, 0)}
GOAL = (3, 3)
A = 4
D = [(-1, 0) if a == 3 else (1, 0) if a == 1 else (0, -1) if a == 0 else (0, 1)
     for a in range(A)]

def step(s, a):
    r, c = s[0] + D[a][0], s[1] + D[a][1]
    r, c = min(max(r, 0), N - 1), min(max(c, 0), N - 1)
    ns = (r, c)
    if ns == GOAL:  return ns, 1.0, True
    if ns in HOLES: return ns, -1.0, True
    return ns, -0.01, False

Q = np.zeros((N, N, A))
alpha, gamma, eps = 0.6, 0.95, 0.15
rews = []
for ep in range(800):
    s, done, G = (0, 0), False, 0.
    while not done:
        a = rng.integers(A) if rng.random() < eps else int(Q[s].argmax())
        ns, r, done = step(s, a)
        Q[s][a] += alpha * (r + gamma * (0 if done else Q[ns].max())
                            - Q[s][a])
        G += r; s = ns
    rews.append(G)
    if ep in (0, 9, 99, 799):
        print(f"ep {ep}: return {G:.2f}")
print("mean return last 100:", round(float(np.mean(rews[-100:])), 3))
print("greedy policy (L D R U):")
for r in range(N):
    print(" ".join("G" if (r, c) == GOAL else "X" if (r, c) in HOLES
                   else "LDRU"[int(Q[r, c].argmax())] for c in range(N)))
np.save('/tmp/qlearn_Q.npy', Q); np.save('/tmp/qlearn_rews.npy', np.array(rews))
print("saved /tmp/qlearn_Q.npy /tmp/qlearn_rews.npy")
