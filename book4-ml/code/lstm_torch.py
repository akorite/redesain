# code/ch10/lstm_torch.py -- nn.LSTM char-LM on the same corpus,
# printed alongside trigram and scratch-RNN perplexities.
# Run from the repository root:  python3 code/ch10/lstm_torch.py
import torch, time
from torch import nn

text = open('data/tiny_shakespeare.txt').read()[:200_000]
vocab = sorted(set(text)); C = len(vocab)
ix = {c: i for i, c in enumerate(vocab)}
data = torch.tensor([ix[c] for c in text])
split = int(0.9 * len(data))
tr, te = data[:split], data[split:]
seq_len = 50

model = nn.Sequential(nn.Embedding(C, 64))
lstm = nn.LSTM(64, 128, batch_first=True)
head = nn.Linear(128, C)
opt = torch.optim.Adam(list(model.parameters()) +
                       list(lstm.parameters()) +
                       list(head.parameters()), lr=2e-3)
lf = nn.CrossEntropyLoss()

def batch(src, n=64):
    s = torch.randint(0, len(src) - seq_len - 1, (n,))
    x = torch.stack([src[i:i+seq_len] for i in s])
    y = torch.stack([src[i+1:i+seq_len+1] for i in s])
    return x, y

def ppl(src):
    model.eval(); lstm.eval()
    with torch.no_grad():
        tot, cnt = 0., 0
        for i in range(0, len(src) - seq_len, 1000):
            x, y = batch(src[i:i+1001], n=20)
            h, _ = lstm(model(x))
            tot += lf(head(h).reshape(-1, C), y.reshape(-1)).item()
            cnt += 1
    return torch.exp(torch.tensor(tot / cnt)).item()

t0 = time.time()
for it in range(801):
    x, y = batch(tr)
    h, _ = lstm(model(x))
    loss = lf(head(h).reshape(-1, C), y.reshape(-1))
    opt.zero_grad(); loss.backward(); opt.step()
    if it % 200 == 0:
        print(f"it {it:>3}: train loss {loss.item():.3f}  "
              f"({time.time()-t0:.0f}s)")

print(f"\nheld-out perplexity (200k-slice tail): {ppl(te):.1f}")

# the honest comparison: same held-out slice the trigram was scored on
full = open('data/tiny_shakespeare.txt').read()
# NOTE: our model was trained on the 200k slice's vocab; for the shared
# 115k slice we reuse the same indexing (chars unseen in the 200k slice
# get skipped -- <1% of characters).
ixf = {c: i for i, c in enumerate(vocab)}
te115 = torch.tensor([ixf[c] for c in full[900_000:1_015_394]
                      if c in ixf])
model.eval(); lstm.eval(); tot = cnt = 0
with torch.no_grad():
    for i in range(0, len(te115) - seq_len, 500):
        s = torch.arange(i, min(i+500, len(te115)-seq_len-1))
        x = torch.stack([te115[j:j+seq_len] for j in s])
        y = torch.stack([te115[j+1:j+seq_len+1] for j in s])
        h, _ = lstm(model(x))
        tot += lf(head(h).reshape(-1, C), y.reshape(-1)).item(); cnt += 1
print("\nthree-way (apples-to-apples where possible):")
print("  trigram (lst 1):      ppl 7.6  (115k disjoint held-out)")
print("  scratch RNN h=64:     ppl 9.0  (train-window ppl -- "
      "not held-out)")
print(f"  torch LSTM h=128:     ppl {torch.exp(torch.tensor(tot/cnt)).item():.1f}  "
      "(same 115k held-out)")

# sample
model.eval()
h = torch.zeros(1, 1, 128); c = torch.zeros(1, 1, 128)
x = torch.tensor([[ix['T']]]); out = 'T'
for _ in range(200):
    e = model(x); o, (h, c) = lstm(e, (h, c))
    p = torch.softmax(head(o[0, -1]), 0)
    ch = torch.multinomial(p, 1).item()
    out += vocab[ch]; x = torch.tensor([[ch]])
print("\n--- LSTM sample ---")
print(out)
