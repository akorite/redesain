"""Real Hyperliquid BTC funding, 500h snapshot (pinned data/hl_funding_btc.json)."""
import json
import numpy as np
d=json.load(open("data/hl_funding_btc.json"))
f=np.array([float(x["fundingRate"]) for x in d])
p=np.array([float(x["premium"]) for x in d])
print(f"{len(d)} hourly funding prints  {d[0]['time']} .. {d[-1]['time']}")
print(f"funding rate: mean {f.mean()*1e4:+.3f}bp/h  sd {f.std()*1e4:.3f}bp  "
      f"min {f.min()*1e4:+.2f}bp  max {f.max()*1e4:+.2f}bp")
print(f"f>0: {(f>0).mean()*100:.0f}% of hours   f=+0.125bp exact: "
      f"{(np.isclose(f,0.0000125)).mean()*100:.0f}%")
print(f"premium: mean {p.mean()*1e4:+.1f}bp   mean(f - premium) = "
      f"{np.mean(f-p)*1e4:+.2f}bp ~ the 1.25bp/8h interest floor")
print(f"annualised carry at mean rate: {f.mean()*24*365*100:+.1f}%")
# a short-perp holding 1 BTC notional earns sum(f)
print(f"30d-equivalent carry: {f.sum()*1e4:.0f}bp of notional over {len(d)}h")
