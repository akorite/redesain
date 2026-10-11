"""ch15: 1-D scalar wave equation u_tt = c^2 u_xx on a lattice; launch
a Gaussian pulse, measure its propagation speed, compare with theory."""
import math

N, c = 400, 1.0
dx = 1.0
dt = 0.7*dx/c          # CFL: must stay < dx/c
u  = [0.0]*N
un = [0.0]*N
up = [0.0]*N
# initial gaussian pulse centred at x0
x0 = 60
for i in range(N):
    u[i] = math.exp(-((i-x0)/8)**2)
    up[i] = u[i]                        # zero initial velocity

def step():
    global up, u, un
    r = (c*dt/dx)**2
    for i in range(1, N-1):
        un[i] = 2*u[i] - up[i] + r*(u[i+1]-2*u[i]+u[i-1])
    un[0] = un[N-1] = 0.0
    up, u, un = u, un, up

def peak(uu):
    return max(range(N), key=lambda i: uu[i])

t = 0.0
marks = []
for s in range(300):
    step(); t += dt
    if s in (0, 99, 199, 299):
        marks.append((round(t,1), peak(u)))
print("pulse peak positions:", marks)
for (t1,p1),(t2,p2) in zip(marks, marks[1:]):
    print(f"  measured v = {(p2-p1)/(t2-t1):.4f} cells/s  (theory c={c})")
print(f"dt/dx CFL = {dt*c/dx:.2f} (must be < 1)")
