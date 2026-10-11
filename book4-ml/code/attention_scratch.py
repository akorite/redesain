# attention_scratch.py -- scaled dot-product attention from tensor
# primitives: no nn.MultiheadAttention allowed (USAAIO-style).
import torch, math

torch.manual_seed(0)

def sdp_attention(Q, K, V, mask=None):
    """softmax(QK^T/sqrt(dk)) V, all in tensor primitives."""
    dk = Q.size(-1)
    scores = Q @ K.transpose(-2, -1) / math.sqrt(dk)   # (..., T, T)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))
    A = torch.softmax(scores, dim=-1)
    return A @ V, A

# ---- the 4-token worked example ------------------------------------
T, dm, dh = 4, 8, 2          # 4 tokens, d_model 8, 2 heads
x = torch.randn(T, dm) * 2.5
Wq, Wk, Wv = (torch.randn(dm, dm) * 0.3 for _ in range(3))
Q, K, V = x @ Wq, x @ Wk, x @ Wv
Qh = Q.view(T, dh, dm // dh).transpose(0, 1)   # (h, T, d/h)
Kh = K.view(T, dh, dm // dh).transpose(0, 1)
Vh = V.view(T, dh, dm // dh).transpose(0, 1)
causal = torch.tril(torch.ones(T, T))           # causal mask
for h in range(dh):
    O, A = sdp_attention(Qh[h], Kh[h], Vh[h], causal)
    print(f"head {h} attention weights (causal):")
    for i in range(T):
        print("  tok%d:" % i, " ".join(f"{a:5.3f}" for a in A[i].tolist()))
O = torch.cat([sdp_attention(Qh[h], Kh[h], Vh[h], causal)[0]
               for h in range(dh)], dim=-1)      # (T, dm) concat heads
print("output row 0 (tok0 attends only itself):",
      " ".join(f"{v:+.3f}" for v in O[0].tolist()))

# ---- independent reference check: brute force in plain python ------
import numpy as np
qs = (x @ Wq).detach().numpy(); ks = (x @ Wk).numpy(); vs = (x @ Wv).numpy()
ref = np.zeros((T, dm))
for h in range(dh):
    sl = slice(h * dm // dh, (h + 1) * dm // dh)
    for i in range(T):
        w = np.array([math.exp(qs[i, sl] @ ks[j, sl]
                      / math.sqrt(dm // dh)) for j in range(i + 1)])
        w /= w.sum()
        ref[i, sl] = w @ vs[: i + 1, sl]
print("max |scratch - numpy reference| =",
      float(np.abs(O.numpy() - ref).max()))

# ---- mask-leak failure analysis ------------------------------------
# a leaked mask lets token i see the future; detect it via
# anachronistically-low reconstruction error on a copy task.
rng = torch.manual_seed(1)
seq = torch.randn(1, 6, 4)
good, _ = sdp_attention(seq, seq, seq, torch.tril(torch.ones(6, 6)))
leak, _ = sdp_attention(seq, seq, seq)            # no mask = leak
err_good = float((good[:, 0] - seq[:, 0]).pow(2).mean())
print(f"causal mask: tok0 sees itself only -> recon err {err_good:.4f}")
print(f"leaked mask: tok0 sees the future -> recon err "
      f"{float((leak[:, 0]-seq[:,0]).pow(2).mean()):.4f}  (leak!)")
