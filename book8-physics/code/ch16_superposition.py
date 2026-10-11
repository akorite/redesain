"""ch16: (a) two counter-propagating waves -> standing wave: snapshot
the envelope at quarter periods, show nodes/antinodes; (b) beats:
f1+f2 -> envelope period check."""
import math

# (a) standing wave on x in [0,L]
L = 1.0
k, w = 2*math.pi/L, 6.28
def y(x,t):
    return math.sin(k*x-w*t) + math.sin(k*x+w*t)
print("standing wave snapshots y(x,t), x in [0,1]:")
for t in (0.0, 0.125, 0.25, 0.375):
    row = " ".join(f"{y(x,t):+.2f}" for x in (0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1.0))
    print(f" t={t:.3f}: {row}")
print("node check x=0.5:", all(abs(y(0.5,t))<1e-9 for t in (0.0,0.31,0.62)))
print("antinode x=0.25 swing:", [round(y(0.25,t),2) for t in (0.0,0.125,0.25)])

# (b) beats
f1, f2 = 440, 444
def s(t): return math.sin(2*math.pi*f1*t)+math.sin(2*math.pi*f2*t)
# envelope via RMS over a 30 ms window (many carrier periods)
ts = [i*5e-4 for i in range(1600)]          # 0.8 s
win = int(0.03/5e-4)
env, ets = [], []
for i in range(win, len(ts)-win):
    m = sum(s(t)**2 for t in ts[i-win:i+win])/(2*win)
    env.append(math.sqrt(2*m))
    ets.append(ts[i])
print("\nbeat: f1 =", f1, " f2 =", f2)
print("env at t=0,.06,.125,.19,.25,.31,.375:", [round(env[min(range(len(ets)), key=lambda i: abs(ets[i]-t))],2) for t in (0,0.06,0.125,0.19,0.25,0.31,0.375)])
# node clusters: where envelope < 0.3
nodes, cur = [], []
for t,e in zip(ets,env):
    if e < 0.7: cur.append(t)
    elif cur: nodes.append(sum(cur)/len(cur)); cur=[]
if cur: nodes.append(sum(cur)/len(cur))
print("envelope nodes at t =", [round(t,3) for t in nodes])
if len(nodes) > 1:
    print("measured beat period = node spacing =", round(nodes[1]-nodes[0],3), " theory 1/|f1-f2| =", round(1/abs(f2-f1),3))
