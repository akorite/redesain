# attn_vs_lib.py -- our from-primitives attention vs
# nn.MultiheadAttention with the same weights: printed agreement.
import torch, torch.nn as nn, math
from attention_scratch import sdp_attention   # reuse, don't duplicate

torch.manual_seed(0)
T, dm, h = 6, 8, 2
x = torch.randn(1, T, dm)
mha = nn.MultiheadAttention(dm, h, bias=False, batch_first=True)

# transplant the library's packed in_proj weights into ours
W = mha.in_proj_weight.detach()            # (3*dm, dm): Q|K|V
Wq, Wk, Wv = W[:dm], W[dm:2 * dm], W[2 * dm:]
q = (x @ Wq.T).view(1, T, h, dm // h).transpose(1, 2)
k = (x @ Wk.T).view(1, T, h, dm // h).transpose(1, 2)
v = (x @ Wv.T).view(1, T, h, dm // h).transpose(1, 2)
causal = torch.tril(torch.ones(T, T))
outs = [sdp_attention(q[:, i], k[:, i], v[:, i], causal)[0]
        for i in range(h)]
ours = torch.cat(outs, -1) @ mha.out_proj.weight.T

mask = ~torch.tril(torch.ones(T, T, dtype=torch.bool))  # library mask
lib, lib_w = mha(x, x, x, attn_mask=mask, need_weights=True)
print("max |scratch - nn.MultiheadAttention| =",
      float((ours - lib).abs().max()))
print("library returned attn weights shape:", tuple(lib_w.shape))
print("verdict: torch.allclose ->",
      bool(torch.allclose(ours, lib, atol=1e-6)))
