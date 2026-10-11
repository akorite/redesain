# code/ch10/trigram_lm.py -- a character trigram language model:
# count -> smooth -> sample at three temperatures -> perplexity.
# Run from the repository root:  python3 code/ch10/trigram_lm.py
import numpy as np

text = open('data/tiny_shakespeare.txt').read()
train, test = text[:900_000], text[900_000:1_015_394]
vocab = sorted(set(text)); C = len(vocab)
ix = {c: i for i, c in enumerate(vocab)}
tr = np.array([ix[c] for c in train])
tt = np.array([ix[c] for c in test])
print(f"chars: train {len(tr):,}  test {len(tt):,}  |V| {C}")

# --- count trigrams p(z | x,y) with add-alpha smoothing ----------------
alpha = 0.1
counts = np.ones((C, C, C)) * alpha
for a, b, c in zip(tr[:-2], tr[1:-1], tr[2:]):
    counts[a, b, c] += 1
P = counts / counts.sum(2, keepdims=True)

def sample(ctx, n=160, tau=1.0, seed=0):
    rng = np.random.default_rng(seed)
    a, b = ix[ctx[0]], ix[ctx[1]]
    out = list(ctx)
    for _ in range(n):
        p = P[a, b] ** (1 / tau); p /= p.sum()
        c = rng.choice(C, p=p); out.append(vocab[c]); a, b = b, c
    return ''.join(out)

def perplexity(seq):
    ll = sum(np.log(P[seq[i-2], seq[i-1], seq[i]]) for i in range(2, len(seq)))
    return np.exp(-ll / (len(seq) - 2))

print(f"trigram perplexity on held-out 115k chars: {perplexity(tt):.1f}")
for tau in [0.5, 1.0, 1.5]:
    print(f"\n--- tau={tau} ---")
    print(sample('To', 160, tau))
