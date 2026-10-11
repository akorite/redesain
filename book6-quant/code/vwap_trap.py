import numpy as np
# designed trap: quiet tape all day, then close-volume spike + price pop
n=390
vol = np.ones(n); vol[-30:]=15; vol=vol/vol.sum()         # 30-min close auction dominates
px_flat = np.full(n,100.0)
px_pop  = np.full(n,100.0); px_pop[-30:]=np.linspace(100,101.5,30)
for tag,px in [("flat tape",px_flat),("close-pop tape",px_pop)]:
    tw = px.mean(); vw = (px*vol).sum()
    print(f"{tag:>14}: TWAP {tw:.4f}  VWAP {vw:.4f}  VWAP-TWAP {(vw-tw)*1e4:+.1f}bp (buyer)")
# the asymmetry: VWAP cannot dodge the auction it is designed to join
print("VWAP tracks volume -- it buys the top when volume+price spike")
