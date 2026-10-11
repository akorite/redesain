import numpy as np

np.seterr(all="ignore")  # Accelerate BLAS prints spurious fp warnings

def blocked_matmul(A, B, b):
    n = A.shape[0]
    assert A.shape == (n, n) and B.shape == (n, n) and n % b == 0
    C = np.zeros((n, n))
    for i in range(0, n, b):
        for j in range(0, n, b):
            for k in range(0, n, b):
                C[i:i+b, j:j+b] += np.matmul(A[i:i+b, k:k+b],
                                             B[k:k+b, j:j+b])
    return C

n, b = 512, 64
rng = np.random.default_rng(2)
A, B = rng.standard_normal((n, n)), rng.standard_normal((n, n))
C = blocked_matmul(A, B, b)
print("agrees with np.matmul:", np.allclose(C, np.matmul(A, B)))
