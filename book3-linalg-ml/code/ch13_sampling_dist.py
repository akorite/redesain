import numpy as np
rng = np.random.default_rng(0)
# estimator of sigma^2: biased /n vs unbiased /(n-1), n=5, 20k datasets
n, sigma2 = 5, 4.0
X = rng.normal(0, np.sqrt(sigma2), (20000, n))
mle = X.var(axis=1, ddof=0)      # /n
unb = X.var(axis=1, ddof=1)      # /(n-1)
print("mean of /n estimator : %.3f  (bias %.3f, theory -0.8)"
      % (mle.mean(), mle.mean()-sigma2))
print("mean of /n-1 estim.  : %.3f" % unb.mean())
print("var of /n estimator  : %.3f   var of /n-1: %.3f"
      % (mle.var(), unb.var()))
print("sample-mean estimator: mean %.4f var %.4f (theory var %.4f)"
      % (X.mean(axis=1).mean(), X.mean(axis=1).var(), sigma2/n))
