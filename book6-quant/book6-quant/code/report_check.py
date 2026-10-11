# a linter for research writeups: required fields in a results memo
import sys
REQUIRED = ["hypothesis","data","window","costs","n_trials","metrics","holdout","risks","repro"]
memo = """hypothesis: funding carry positive on BTC
data: HL fundingHistory 500h pinned
window: 2025-05 to 2025-06
costs: 5bp fee + 2bp slip
n_trials: 1
metrics: mean +0.113bp/h, 85% at floor
holdout: none (descriptive)
risks: venue rule change, funding flip
repro: funding_hist.py data/hl_funding_btc.json
"""
missing=[k for k in REQUIRED if f"{k}:" not in memo]
print(f"memo check: {len(REQUIRED)-len(missing)}/{len(REQUIRED)} fields present")
print(f"missing: {missing if missing else 'none'}")
print("the checklist is the deliverable -- a memo without fields is a story")
