"""ch03: microprice = size-weighted mid, the informed mid."""
def microprice(bid_p, bid_q, ask_p, ask_q):
    return (ask_p * bid_q + bid_p * ask_q) / (bid_q + ask_q)

cases = [
    ("balanced   ", 100.0, 4, 100.5, 2),
    ("ask heavy  ", 100.0, 4, 100.5, 40),
    ("bid heavy  ", 100.0, 40, 100.5, 2),
]
for tag, bp, bq, ap, aq in cases:
    mp = microprice(bp, bq, ap, aq)
    mid = (bp + ap) / 2
    print(f"{tag} book ({bq}@{bp} | {aq}@{ap}): mid={mid:.4f} "
          f"microprice={mp:.4f}  drift hint {mp-mid:+.4f}")
