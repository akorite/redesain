# diffusion2d.py -- toy DDPM on a 2-D spiral: forward noising,
# a small score net, and the denoising trajectory as the lesson.
import numpy as np, torch, torch.nn as nn, torch.nn.functional as F

torch.manual_seed(0); np.random.seed(0)
n = 4000
t_ = np.linspace(0, 4 * np.pi, n)
X = np.stack([t_ * np.cos(t_), t_ * np.sin(t_)], 1) / 12.6
X += np.random.randn(n, 2) * 0.15
X = torch.tensor(X, dtype=torch.float32)

T = 50
betas = torch.linspace(1e-4, 0.02, T)
alphas = 1 - betas
abar = torch.cumprod(alphas, 0)

class Score(nn.Module):
    def __init__(s):
        super().__init__()
        s.f = nn.Sequential(nn.Linear(3, 128), nn.GELU(),
                            nn.Linear(128, 128), nn.GELU(), nn.Linear(128, 2))
    def forward(s, x, tt):
        return s.f(torch.cat([x, tt[:, None] / T], 1))

m = Score(); opt = torch.optim.Adam(m.parameters(), 2e-3)
for it in range(2001):
    i = torch.randint(len(X), (256,))
    t = torch.randint(1, T, (256,), dtype=torch.float32)
    ti = t.long()
    noise = torch.randn(256, 2)
    xt = (abar[ti, None].sqrt() * X[i]
          + (1 - abar[ti, None]).sqrt() * noise)
    loss = F.mse_loss(m(xt, t), noise)
    opt.zero_grad(); loss.backward(); opt.step()
    if it % 500 == 0 or it == 2000:
        print(f"it {it}: noise-pred loss {loss.item():.4f}")

# ancestral sampling, saving the trajectory
m.eval()
x = torch.randn(400, 2); traj = [x.clone()]
with torch.no_grad():
    for tt in range(T - 1, 0, -1):
        eps = m(x, torch.full((400,), tt, dtype=torch.float32))
        x = (x - (1 - alphas[tt]) / (1 - abar[tt]).sqrt() * eps) \
            / alphas[tt].sqrt()
        if tt > 1:
            x += betas[tt].sqrt() * torch.randn(400, 2)
        if tt % 10 == 0 or tt == 1:
            traj.append(x.clone())
np.save('diff_traj.npy', np.stack([a.numpy() for a in traj]))
print(f"saved trajectory: {len(traj)} panels, T={T} steps, "
      f"final spread {float(x.std()):.2f} vs data {float(X.std()):.2f}")
