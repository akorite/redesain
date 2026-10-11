# judge_bias_test.py -- the paired-ordering protocol for LLM-as-judge
# bias, run on stub judges that carry REAL documented biases
# (position and length), so the flip rates are measured, not asserted.
# With an API-backed judge you'd swap judge(a,b) -- protocol identical.
import numpy as np

rng = np.random.default_rng(0)

# ---- a corpus of candidate pairs: (text_a, text_b, true_quality_a) --
# qualities are latent; the judge sees only text + position.
PAIRS = []
for i in range(200):
    qa, qb = rng.uniform(0.3, 0.9), rng.uniform(0.3, 0.9)
    la = int(20 + 60 * rng.random())          # answer lengths
    lb = int(20 + 60 * rng.random())
    PAIRS.append(dict(q=(qa, qb), L=(la, lb)))

def make_judge(bias_kind, w_pos=0.15, w_len=0.004):
    """returns judge(A,B)->0/1: which answer it prefers.
    quality + biases: position bonus, length bonus."""
    def judge(qA, lA, qB, lB):
        sA = qA + (w_pos if bias_kind == 'position' else 0) + w_len * lA
        sB = qB - (w_pos if bias_kind == 'position' else 0) + w_len * lB
        return 0 if sA >= sB else 1
    return judge

def flip_rate(judge):
    """fraction of pairs whose verdict changes when order swaps."""
    flips = 0
    for p in PAIRS:
        a_first = judge(p['q'][0], p['L'][0], p['q'][1], p['L'][1])
        b_first = judge(p['q'][1], p['L'][1], p['q'][0], p['L'][0])
        if a_first != 1 - b_first:
            flips += 1
    return flips / len(PAIRS)

def length_winner_rate(judge):
    """how often the LONGER answer wins."""
    wins = 0
    for p in PAIRS:
        w = judge(p['q'][0], p['L'][0], p['q'][1], p['L'][1])
        longer = 0 if p['L'][0] > p['L'][1] else 1
        wins += (w == longer)
    return wins / len(PAIRS)

def accuracy(judge):
    """verdict vs the true quality ordering."""
    ok = 0
    for p in PAIRS:
        w = judge(p['q'][0], p['L'][0], p['q'][1], p['L'][1])
        true = 0 if p['q'][0] > p['q'][1] else 1
        ok += (w == true)
    return ok / len(PAIRS)

print(f"{'judge':22s} {'acc':>5s} {'flip':>5s} {'long-wins':>9s}")
for name, kind in [('neutral (no bias)', 'none'),
                   ('position-biased', 'position'),
                   ('length-biased', 'length'),
                   ('both biases', 'both')]:
    j = make_judge(kind if kind != 'none' else '')
    if kind == 'length':
        j = make_judge('none', w_len=0.02)
    if kind == 'both':
        j = make_judge('position', w_len=0.02)
    print(f"{name:22s} {accuracy(j):5.2f} {flip_rate(j):5.2f} {length_winner_rate(j):9.2f}")

print("\nprotocol: verdict must be a permutation-invariant function;")
print("any flip on swapped order = position-dependent judge.")
