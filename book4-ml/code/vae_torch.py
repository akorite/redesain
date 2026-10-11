# vae_torch.py -- a small VAE on `digits`, ELBO-trained in ~20s.
# Encoder 64->128->(mu,logvar,z8), decoder z8->128->64 (sigmoid recon).
import torch, torch.nn as nn, torch.nn.functional as F, numpy as np
from sklearn.datasets import load_digits

torch.manual_seed(0); np.random.seed(0)
X = torch.tensor(load_digits().images.reshape(-1, 64) / 16.,
                 dtype=torch.float32)
tr = X[:1400]

class VAE(nn.Module):
    def __init__(s):
        super().__init__()
        s.e1 = nn.Linear(64, 128); s.mu = nn.Linear(128, 8)
        s.lv = nn.Linear(128, 8)
        s.d1 = nn.Linear(8, 128); s.d2 = nn.Linear(128, 64)
    def enc(s, x):
        h = F.relu(s.e1(x)); return s.mu(h), s.lv(h)
    def dec(s, z):
        return torch.sigmoid(s.d2(F.relu(s.d1(z))))
    def forward(s, x):
        mu, lv = s.enc(x)
        z = mu + torch.exp(0.5 * lv) * torch.randn_like(lv)  # reparam
        return s.dec(z), mu, lv

m = VAE(); opt = torch.optim.Adam(m.parameters(), 3e-3)
for it in range(2001):
    xb = tr[torch.randint(len(tr), (64,))]
    rec, mu, lv = m(xb)
    bce = F.binary_cross_entropy(rec, xb, reduction='sum') / 64
    kld = -0.5 * (1 + lv - mu.pow(2) - lv.exp()).sum(1).mean()
    loss = bce + kld
    opt.zero_grad(); loss.backward(); opt.step()
    if it % 500 == 0 or it == 2000:
        print(f"it {it}: loss {loss.item():.1f}  bce {bce.item():.1f}"
              f"  kld {kld.item():.1f}")

# latent traversal: sweep z[0] and z[1] over the prior's range
m.eval()
with torch.no_grad():
    z = torch.zeros(8, 8);  g = torch.linspace(-2, 2, 8)
    zz = torch.stack([torch.tensor([g[j], g[i]] + [0]*6)
                      for i in range(8) for j in range(8)])
    grid = m.dec(zz).reshape(8, 8, 8, 8)
    np.save('vae_grid.npy', grid.numpy().transpose(0, 2, 1, 3)
            .reshape(64, 64))
    zr = torch.randn(24, 8)
    np.save('vae_samples.npy', m.dec(zr).reshape(-1, 8, 8).numpy())
    # honesty probe: nearest-neighbour distance of samples to training
    rec_s = m.dec(zr).reshape(24, -1)
    dists = ((rec_s[:, None] - tr[None]).pow(2).sum(-1).min(-1).values)
    print(f"sample->nearest-train L2: mean {dists.sqrt().mean():.2f} "
          f"min {dists.sqrt().min():.2f} (0 would be memorisation)")
