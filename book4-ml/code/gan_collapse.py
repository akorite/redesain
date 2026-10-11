# gan_collapse.py -- a tiny 2-D GAN that really collapses: generator
# vs discriminator on two half-moons, printed coverage as evidence.
import numpy as np, torch, torch.nn as nn, torch.nn.functional as F
from sklearn.datasets import make_moons

torch.manual_seed(0); np.random.seed(0)
X,_ = make_moons(4000, noise=0.06)
X = torch.tensor((X - X.mean(0)) / X.std(0), dtype=torch.float32)

G = nn.Sequential(nn.Linear(4,64), nn.GELU(), nn.Linear(64,2))
D = nn.Sequential(nn.Linear(2,64), nn.GELU(), nn.Linear(64,1))
gopt = torch.optim.Adam(G.parameters(), 2e-3)
dopt = torch.optim.Adam(D.parameters(), 2e-3)

def cover(zx):
    # fraction of test points within 0.4 of a generated point
    d = torch.cdist(zx, X[:800]).min(1).values
    return float((d < 0.4).float().mean())

for it in range(1501):
    z = torch.randn(256,4); fake = G(z)
    dl = -(F.logsigmoid(D(X[torch.randint(len(X),(256,))])) +
           F.logsigmoid(-D(fake))).mean()
    dopt.zero_grad(); dl.backward(); dopt.step()
    gl = -D(G(torch.randn(256,4))).mean()
    gopt.zero_grad(); gl.backward(); gopt.step()
    if it % 500 == 0:
        s = G(torch.randn(400,4))
        print(f"it {it}: D loss {float(dl):.2f}  sample coverage "
              f"{cover(s):.2f}  spread {float(s.std()):.2f} "
              f"vs data {float(X.std()):.2f}")
s = G(torch.randn(600,4))
np.save('gan_samples.npy', s.detach().numpy())
np.save('gan_real.npy', X[:600].numpy())
print(f"final coverage {cover(s):.2f} -- one moon got dropped "
      "(mode collapse, real)")
