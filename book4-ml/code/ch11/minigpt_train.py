# minigpt_train.py -- a miniature character-level GPT on Tiny
# Shakespeare: the transformer block built from our own attention,
# then trained ~2 min on CPU. Positional ablation included.
import torch, torch.nn as nn, torch.nn.functional as F, math, time

torch.manual_seed(0)
B, T, C, NH, NL, LR, ITERS = 32, 64, 96, 4, 2, 3e-3, 600

text = open('../../data/tiny_shakespeare.txt').read()[:200_000]
vocab = sorted(set(text)); V = len(vocab)
stoi = {c: i for i, c in enumerate(vocab)}
itos = {i: c for c, i in stoi.items()}
data = torch.tensor([stoi[c] for c in text])
enc = lambda s: torch.tensor([stoi[c] for c in s])
dec = lambda t: ''.join(itos[int(i)] for i in t)

def batch():
    ix = torch.randint(len(data) - T - 1, (B,))
    return (torch.stack([data[i:i + T] for i in ix]),
            torch.stack([data[i + 1:i + T + 1] for i in ix]))

class Head(nn.Module):
    def __init__(s, hsz):
        super().__init__()
        s.q, s.k, s.v = (nn.Linear(C, hsz, bias=False) for _ in range(3))
        s.register_buffer('m', torch.tril(torch.ones(T, T)))
    def forward(s, x):
        q, k, v = s.q(x), s.k(x), s.v(x)
        a = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        a = a.masked_fill(s.m[:x.size(1), :x.size(1)] == 0, float('-inf'))
        w = F.softmax(a, -1)
        s.last_w = w
        return w @ v

class Block(nn.Module):
    def __init__(s):
        super().__init__()
        s.heads = nn.ModuleList([Head(C // NH) for _ in range(NH)])
        s.proj, s.ln1, s.ln2 = nn.Linear(C, C), nn.LayerNorm(C), nn.LayerNorm(C)
        s.ff = nn.Sequential(nn.Linear(C, 4 * C), nn.GELU(), nn.Linear(4 * C, C))
    def forward(s, x):
        x = x + s.proj(torch.cat([h(x) for h in s.heads], -1))
        return x + s.ff(s.ln2(s.ln1(x)))

class MiniGPT(nn.Module):
    def __init__(s, pos=True):
        super().__init__()
        s.te = nn.Embedding(V, C)
        s.pe = nn.Embedding(T, C) if pos else None
        s.bl = nn.ModuleList([Block() for _ in range(NL)])
        s.ln, s.fc = nn.LayerNorm(C), nn.Linear(C, V)
    def forward(s, idx, y=None):
        x = s.te(idx) + (s.pe.weight[:idx.size(1)] if s.pe is not None else 0)
        for b in s.bl: x = b(x)
        lo = s.fc(s.ln(x))
        l = F.cross_entropy(lo.view(-1, V), y.view(-1)) if y is not None else None
        return lo, l

def train(m, iters, tag):
    opt = torch.optim.AdamW(m.parameters(), lr=LR)
    t0 = time.time()
    for i in range(iters + 1):
        xb, yb = batch()
        _, loss = m(xb, yb)
        opt.zero_grad(); loss.backward(); opt.step()
        if i % 200 == 0 or i == iters:
            print(f"{tag} it {i}: loss {loss.item():.3f}")
    print(f"{tag} {time.time()-t0:.0f}s")
    return m

m = train(MiniGPT(), ITERS, "gpt")
print("params:", sum(p.numel() for p in m.parameters()))
m_abl = train(MiniGPT(pos=False), 300, "no-pos")

# perplexity on the shared held-out slice (same slice as ch10)
test = open('../../data/tiny_shakespeare.txt').read()[-115_394:]
xtest = torch.tensor([stoi.get(c, 0) for c in test])
with torch.no_grad():
    nll, cnt = 0., 0
    for i in range(0, len(xtest) - T - 1, 1000):
        _, l = m(xtest[i:i+T][None], xtest[i+1:i+T+1][None]); nll += float(l); cnt += 1
    print(f"held-out loss/char {nll/cnt:.3f}  ppl {math.exp(nll/cnt):.1f} (115k slice)")

ctx = enc("To be or not to be, ")
with torch.no_grad():
    idx = ctx[None]
    for _ in range(160):
        lo, _ = m(idx[:, -T:])
        p = F.softmax(lo[0, -1] / 0.9, -1)
        idx = torch.cat([idx, torch.multinomial(p, 1)[None]], 1)
print("--- gpt sample ---"); print(dec(idx[0]))

torch.save({f"h{h}": m.bl[-1].heads[h].last_w[0].numpy()
            for h in range(NH)}, "attn_weights.pt")
print("attention weights for last block saved (4 heads, real)")
