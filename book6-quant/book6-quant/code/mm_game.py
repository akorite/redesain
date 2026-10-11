"""ch03 WE2: market-making game. MM quotes +/-half-spread around mid.
Compare average PnL vs flow where an informed share trades only when
the next move covers the spread. 24 seeds each."""
import numpy as np

T, S, drift_sig = 3000, 0.10, 0.05

def run(share, seed):
    rng = np.random.default_rng(seed)
    fair, inv, cash = 100.0, 0, 0.0
    pnl_inf, n_inf = [], 0
    for _ in range(T):
        nxt = fair + rng.normal(0, drift_sig)
        informed = rng.random() < share
        if informed:      # informed trades only when |move| > S
            side = "b" if nxt - fair > S else \
                   ("s" if fair - nxt > S else None)
        else:
            side = "b" if rng.random() < 0.5 else "s"
        if side is None:
            fair = nxt; continue
        if side == "b":
            inv -= 1; cash += fair + S      # MM sells at ask
            pnl_inf.append(S - (nxt - fair)) if informed else None
        else:
            inv += 1; cash -= fair - S      # MM buys at bid
            pnl_inf.append(S - (fair - nxt)) if informed else None
        if informed: n_inf += 1
        fair = nxt
    return cash + inv * fair, np.mean(pnl_inf) if n_inf else 0.0

for share in (0.0, 0.3, 0.6, 0.9):
    res = [run(share, s) for s in range(24)]
    pnl = np.mean([r[0] for r in res])
    pi = np.mean([r[1] for r in res]) if share else 0.0
    print(f"informed share {share:.1f}: mean MM PnL {pnl:+9.2f} | "
          f"mean PnL per informed trade {pi:+6.3f}")
print("(uninformed flow pays the spread; informed flow takes it "
      "back with interest)")
