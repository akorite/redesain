import numpy as np
# MLE for coin: observed 7 heads / 10 flips
ths = np.linspace(0.001, 0.999, 999)
def loglik(t): return 7*np.log(t) + 3*np.log(1-t)
ll = np.array([loglik(t) for t in ths])
mle = ths[ll.argmax()]
print("grid argmax theta = %.3f   (exact 0.7)" % mle)
print("log-lik at .5: %.3f  at .7: %.3f" % (loglik(.5), loglik(.7)))
# second derivative at mle (Fisher info / curvature)
d2 = -7/mle**2 - 3/(1-mle)**2
print("l''(mle) = %.2f (negative -> max)" % d2)
