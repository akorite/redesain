import numpy as np

# the instructive bug: naive sigmoid lets exp() see +709+ -> overflow
def sigmoid_naive(z): return 1/(1+np.exp(-z))

# stable form: exp() only ever sees nonpositive arguments
def sigmoid_stable(z):
    out = np.empty_like(z)
    pos = z >= 0
    out[pos] = 1/(1+np.exp(-z[pos]))
    ez = np.exp(z[~pos]); out[~pos] = ez/(1+ez)
    return out

np.seterr(over='raise')   # make overflow loud
try:
    print("naive at z=-1000:", sigmoid_naive(np.array(-1000.)))
except FloatingPointError as e:
    print("naive at z=-1000 -> FloatingPointError:", e)
print("stable at z=-1000:", sigmoid_stable(np.array(-1000.))[()])
np.seterr(over='warn')

# where the damage lands: softmax over big logits -> inf/inf = nan
logits = np.array([1000., 999.])
with np.errstate(over='ignore', invalid='ignore'):
    e = np.exp(logits)
    sm_naive = e/e.sum()
e2 = np.exp(logits - logits.max())
sm_stable = e2/e2.sum()
print("softmax naive :", sm_naive)
print("softmax stable:", sm_stable)
