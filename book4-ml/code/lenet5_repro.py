# lenet5_repro.py -- reproduce LeNet-5 on MNIST (LeCun 1998 claims ~0.95% test error).
# CPU-feasible: full 60k train set, 3 epochs, Adam. Logged per ch17's lab-notebook protocol.
import torch, torch.nn as nn, time, json, random, numpy as np
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
SEED = 0
random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)
tf = transforms.Compose([transforms.Pad(2), transforms.ToTensor(),
                         transforms.Normalize((0.1307,), (0.3081,))])
tr = datasets.MNIST('/tmp/mnist', train=True, download=True, transform=tf)
te = datasets.MNIST('/tmp/mnist', train=False, transform=tf)
trl, tel = DataLoader(tr, 128, True), DataLoader(te, 512)

class LeNet5(nn.Module):  # C1-S2-C3-S4-C5-F6-Gaussian->approx softmax readout
    def __init__(self):
        super().__init__()
        self.f = nn.Sequential(
            nn.Conv2d(1, 6, 5), nn.Tanh(), nn.AvgPool2d(2),
            nn.Conv2d(6, 16, 5), nn.Tanh(), nn.AvgPool2d(2),
            nn.Conv2d(16, 120, 5), nn.Tanh(), nn.Flatten(),
            nn.Linear(120, 84), nn.Tanh(), nn.Linear(84, 10))
    def forward(self, x): return self.f(x)

net = LeNet5()
opt = torch.optim.Adam(net.parameters(), lr=1e-3)
lossf = nn.CrossEntropyLoss()
t0 = time.time(); hist = []
for ep in range(8):
    net.train()
    for xb, yb in trl:
        opt.zero_grad(); loss = lossf(net(xb), yb)
        loss.backward(); opt.step()
    net.eval(); correct = 0
    with torch.no_grad():
        for xb, yb in tel:
            correct += (net(xb).argmax(1) == yb).sum().item()
    acc = correct / len(te)
    hist.append(acc)
    print(f'epoch {ep}: test acc {acc:.4f} err {1-acc:.4f} t={time.time()-t0:.0f}s')
params = sum(p.numel() for p in net.parameters())
torch.save(net.state_dict(), 'lenet5_state.pt')
json.dump({'seed': SEED, 'epochs': 8, 'opt': 'Adam lr=1e-3', 'params': params,
           'hist': hist, 'final_acc': hist[-1], 'final_err': 1-hist[-1],
           'paper_claim_err': 0.0095, 'wall_s': time.time()-t0},
          open('lenet5_log.json', 'w'), indent=1)
print(f'params {params} | final err {1-hist[-1]:.4f} vs paper 0.0095')
