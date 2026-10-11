# code/ch10/rnn_scratch.py -- a character RNN in raw NumPy:
# forward, truncated BPTT, sampling. ~80 lines of the real thing.
# Run from the repository root:  python3 code/ch10/rnn_scratch.py
import numpy as np

text = open('data/tiny_shakespeare.txt').read()[:200_000]
vocab = sorted(set(text)); C = len(vocab)
ix = {c: i for i, c in enumerate(vocab)}
data = np.array([ix[c] for c in text])
h_size, seq_len, lr = 64, 25, 0.005
rng = np.random.default_rng(7)
Wxh = rng.normal(0, 0.1, (C, h_size))
Whh = rng.normal(0, 0.1, (h_size, h_size))
Why = rng.normal(0, 0.1, (h_size, C))
bh, by = np.zeros(h_size), np.zeros(C)

def softmax(z):
    z = z - z.max(); e = np.exp(z); return e / e.sum()

# targets are the input shifted by one char
ptr, it = 0, 0
losses = []
while it < 4000:
    xs = data[ptr:ptr+seq_len]
    data_targets = data[ptr+1:ptr+seq_len+1]
    if len(xs) < seq_len: ptr, it = 0, it + 1; continue
    xs = np.eye(C)[xs]                    # one-hot rows
    h = np.zeros(h_size)
    # forward
    hs = {-1: h}; ps = {}; loss = 0
    for t in range(seq_len):
        hs[t] = np.tanh(xs[t] @ Wxh + hs[t-1] @ Whh + bh)
        ps[t] = softmax(hs[t] @ Why + by)
        loss -= np.log(ps[t][data_targets[t]] + 1e-12)
    # backward (BPTT)
    dWxh, dWhh, dWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
    dbh, dby = np.zeros_like(bh), np.zeros_like(by)
    dh_next = np.zeros(h_size)
    for t in reversed(range(seq_len)):
        dy = ps[t].copy(); dy[data_targets[t]] -= 1
        dWhy += np.outer(hs[t], dy); dby += dy
        dh = dy @ Why.T + dh_next
        dh_raw = (1 - hs[t]**2) * dh
        dbh += dh_raw; dWxh += np.outer(xs[t], dh_raw)
        dWhh += np.outer(hs[t-1], dh_raw)
        dh_next = dh_raw @ Whh
    for g in [dWxh, dWhh, dWhy, dbh, dby]:
        np.clip(g, -5, 5, out=g)         # gradient clipping
    eff = lr if it < 3000 else lr/5      # decay once it's stable
    Wxh -= eff*dWxh; Whh -= eff*dWhh
    Why -= eff*dWhy; bh -= eff*dbh; by -= eff*dby
    losses.append(loss/seq_len)
    if it % 1000 == 0 or it == 3999:
        print(f"it {it:>4}: loss/char {loss/seq_len:.3f}  "
              f"ppl {np.exp(loss/seq_len):.1f}")
    ptr += seq_len; it += 1
    if ptr + seq_len + 1 >= len(data): ptr = 0

# --- sample ------------------------------------------------------------
def sample(seed_ch='T', n=200):
    h = np.zeros(h_size); x = np.eye(C)[ix[seed_ch]]
    out = seed_ch
    for _ in range(n):
        h = np.tanh(x @ Wxh + h @ Whh + bh)
        p = softmax(h @ Why + by)
        c = np.random.default_rng().choice(C, p=p)
        out += vocab[c]; x = np.eye(C)[c]
    return out

print("\n--- sample after training ---")
print(sample())
