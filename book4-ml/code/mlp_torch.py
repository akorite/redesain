# code/ch07/mlp_torch.py -- same net, gradients for free via autograd,
# then the three-way agreement table.
# Run from the repository root:  python3 code/ch07/mlp_torch.py
import numpy as np, torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X, y = load_digits(return_X_y=True)
X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)
Xt = torch.tensor(Xtr, dtype=torch.float32)
yt = torch.tensor(ytr)
Xe = torch.tensor(Xte, dtype=torch.float32)

torch.manual_seed(7)
net = torch.nn.Sequential(
    torch.nn.Linear(64, 48), torch.nn.ReLU(),
    torch.nn.Linear(48, 10))
opt = torch.optim.SGD(net.parameters(), lr=0.5)
lossf = torch.nn.CrossEntropyLoss()

for ep in range(61):
    if ep % 10 == 0:
        with torch.no_grad():
            l = lossf(net(Xt), yt).item()
            acc = (net(Xe).argmax(1).numpy() == yte).mean()
        print(f"torch epoch {ep:>3}: loss {l:.3f}  test acc {acc:.3f}")
    opt.zero_grad()
    lossf(net(Xt), yt).backward()   # <- the whole chapter in one call
    opt.step()

# --- agreement: same net, three implementations ------------------------
print("\nagreement on the SAME 48-hidden-unit net:")
sk = MLPClassifier(hidden_layer_sizes=(48,), max_iter=200, alpha=0,
                   learning_rate_init=0.1, random_state=7).fit(Xtr, ytr)
print(f"  scratch (60 ep, lr .5): test acc ~0.94-0.95 (listing above)")
print(f"  torch   (60 ep, lr .5): test acc "
      f"{(net(Xe).argmax(1).numpy() == yte).mean():.3f}")
print(f"  sklearn (39 it, lr .1): test acc {sk.score(Xte, yte):.3f}")
print("  (sklearn's lr .5 diverged to 0.102 -- lr is a real dial,")
print("   and each solver's defaults are their own trajectory.)")
