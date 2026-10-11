# drift_detect.py -- PSI + KS on a live feature stream.
# Stream: 3000 benign rows then a real drift (mean shift + heavy tail).
# Question: which statistic catches it, and when?
import numpy as np
from scipy import stats

rng = np.random.default_rng(0)
ref = rng.normal(10., 2., 3000)                      # reference window
live_ok = rng.normal(10., 2., 3000)                  # pre-drift stream
live_bad = np.concatenate([rng.normal(11.5, 2., 1500),   # mean shift
                           rng.standard_t(3, 1500)*2+10]) # heavy tails
stream = np.concatenate([live_ok, live_bad])

def psi(a, b, bins=10):
    """population stability index between two samples."""
    edges = np.quantile(a, np.linspace(0, 1, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    pa = np.histogram(a, edges)[0] / len(a)
    pb = np.histogram(b, edges)[0] / len(b)
    pa = np.clip(pa, 1e-4, None); pb = np.clip(pb, 1e-4, None)
    return float(np.sum((pa - pb) * np.log(pa / pb)))

# rolling detection over 500-row windows
hits = []
for i in range(0, len(stream) - 500, 250):
    w = stream[i:i + 500]
    p = psi(ref, w)
    k = stats.ks_2samp(ref, w).statistic
    hits.append((i, p, k))
    if i % 1500 == 0 or (p > 0.25 and hits[-2][1] <= 0.25):
        print(f"rows {i:5d}-{i+500}: PSI {p:.3f}   KS {k:.3f}")

first_alarm = next(i for i, p, k in hits if p > 0.25)
print(f"PSI>0.25 alarm first at row {first_alarm} "
      f"(drift injected at 3000; lead {3000-first_alarm} rows)")
print(f"max PSI post-drift {max(p for _,p,_ in hits):.3f}; "
      f"max KS post-drift {max(k for _,_,k in hits):.3f}")
np.save('/tmp/drift_hits.npy', np.array(hits))
np.save('/tmp/ref.npy', ref); np.save('/tmp/stream.npy', stream)
