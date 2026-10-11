# code/ch09/cnn_torch.py -- a LeNet-style CNN on a real MNIST subset,
# epoch log printed; vs a dense net of similar parameter count.
# Run from the repository root:  python3 code/ch09/cnn_torch.py
import torch, time
import torchvision as tv
from torch import nn

tr = tv.datasets.MNIST('/tmp/mnist', train=True, download=True,
                       transform=tv.transforms.ToTensor())
te = tv.datasets.MNIST('/tmp/mnist', train=False, download=True,
                       transform=tv.transforms.ToTensor())
tr.data, tr.targets = tr.data[:12000], tr.targets[:12000]
te.data, te.targets = te.data[:2000], te.targets[:2000]
dl = torch.utils.data.DataLoader(tr, batch_size=64, shuffle=True)

cnn = nn.Sequential(
    nn.Conv2d(1, 8, 5), nn.ReLU(), nn.MaxPool2d(2),      # 28->24->12
    nn.Conv2d(8, 16, 3), nn.ReLU(), nn.MaxPool2d(2),     # 12->10->5
    nn.Flatten(),
    nn.Linear(16*5*5, 64), nn.ReLU(), nn.Linear(64, 10))
dense = nn.Sequential(
    nn.Flatten(), nn.Linear(28*28, 512), nn.ReLU(),
    nn.Linear(512, 64), nn.ReLU(), nn.Linear(64, 10))

def params(m): return sum(p.numel() for p in m.parameters())
print(f"params: cnn {params(cnn):,}   dense {params(dense):,}")

def acc(m):
    with torch.no_grad():
        x = te.data.float().unsqueeze(1)/255.
        return (m(x).argmax(1) == te.targets).float().mean().item()

def train(m, name, epochs=3):
    opt = torch.optim.Adam(m.parameters(), lr=1e-3)
    lf = nn.CrossEntropyLoss()
    t0 = time.time()
    for ep in range(epochs):
        tot = 0
        for xb, yb in dl:
            opt.zero_grad(); loss = lf(m(xb), yb)
            loss.backward(); opt.step(); tot += loss.item()
        print(f"{name} ep{ep}: loss {tot/len(dl):.3f}"
              f"  test acc {acc(m):.4f}  ({time.time()-t0:.0f}s)")
    return acc(m)

a = train(cnn, 'cnn  ')
b = train(dense, 'dense')
print(f"\nfinal: cnn {a:.4f} vs dense {b:.4f}  "
      f"(cnn uses {params(cnn)/params(dense):.0%} of dense's params)")
import os
torch.save(cnn.state_dict(),
           os.path.join(os.path.dirname(__file__), 'cnn_state.pt'))
print("saved cnn weights -> code/ch09/cnn_state.pt for filters_viz.py")
