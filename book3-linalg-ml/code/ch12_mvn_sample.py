import numpy as np
np.set_printoptions(precision=3, suppress=True)
rng = np.random.default_rng(2)

Sigma = np.array([[1.0, 0.9], [0.9, 1.0]])
mu = np.array([0., 0.])
# sample via eigendecomposition (ch.9!): X = mu + Q Lambda^1/2 z, z~N(0,I)
lam, Q = np.linalg.eigh(Sigma)
print("eigvals Sigma:", lam)           # PSD check
Z = rng.standard_normal((2, 200_000))
with np.errstate(all="ignore"):        # silences a spurious BLAS warning on some builds
    X = mu[:, None] + (Q * np.sqrt(lam)[None, :]) @ Z
print("sample cov:"); print(np.cov(X))
print("target Sigma:"); print(Sigma)
print("corr:", np.corrcoef(X)[0,1])
