"""ch17: Kac-style 2-D gas thermalization -- each "collision" rotates
the pair's relative velocity by a random angle in the CM frame
(equal-mass elastic collision). Check distribution vs 2-D
Maxwell-Boltzmann: <v^2>, <v>, tail. sigma^2=0.5 per axis."""
import random, math

N = 4000
random.seed(7)
vx = [random.choice([-1.0,1.0]) for _ in range(N)]   # start degenerate: all |v|=1
vy = [0.0]*N

for _ in range(200000):
    i, j = random.randrange(N), random.randrange(N)
    if i == j: continue
    # relative velocity, rotate by random angle
    wx, wy = vx[i]-vx[j], vy[i]-vy[j]
    th = random.random()*2*math.pi
    c, s = math.cos(th), math.sin(th)
    rx, ry = c*wx - s*wy, s*wx + c*wy
    cx, cy = (vx[i]+vx[j])/2, (vy[i]+vy[j])/2
    vx[i], vy[i] = cx + rx/2, cy + ry/2
    vx[j], vy[j] = cx - rx/2, cy - ry/2

speeds = sorted(math.hypot(x,y) for x,y in zip(vx,vy))
msv = sum(s*s for s in speeds)/N
print("mean <v^2> =", round(msv,4), "(1.0: collisions conserve KE)")
print("rms speed   =", round(math.sqrt(msv),4))
print("mean speed  =", round(sum(speeds)/N,4), " 2D MB theory =", round(math.sqrt(math.pi/2)/math.sqrt(2),4))
bins = [0]*10
for s in speeds:
    k = int(s/0.4)
    if k < 10: bins[k]+=1
print("hist (0.4 bins) =", bins)
tail = sum(1 for s in speeds if s > 2.5)/N
print("P(v>2.5) sim =", round(tail,4), " theory exp(-v^2/(2*0.5)) =", round(math.exp(-2.5**2),4))
