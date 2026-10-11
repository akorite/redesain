"""Triple-loop matrix multiplication vs np.matmul: correctness and cost."""
import time
import numpy as np

def matmul(A, B):
    n, k, m = A.shape[0], B.shape[0], B.shape[1]
    C = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            for l in range(k):
                C[i, j] += A[i, l] * B[l, j]
    return C

rng = np.random.default_rng(1)
# macOS Accelerate BLAS emits spurious floating-point warnings inside
# np.matmul on first call; they are not data problems — silence them.
np.seterr(all="ignore")
np.matmul(np.eye(4), np.eye(4))  # warm-up

print(f"{'n':>5} {'ours (s)':>10} {'np (s)':>10} {'agree?':>8}")
for n in [128, 256]:
    A, B = rng.standard_normal((n, n)), rng.standard_normal((n, n))
    t0 = time.perf_counter(); C_ours = matmul(A, B); t1 = time.perf_counter()
    t2 = time.perf_counter(); C_np = np.matmul(A, B); t3 = time.perf_counter()
    ok = np.allclose(C_ours, C_np)
    print(f"{n:>5} {t1-t0:>10.4f} {t3-t2:>10.4f} {str(ok):>8}")
for n in [512, 1024]:
    A, B = rng.standard_normal((n, n)), rng.standard_normal((n, n))
    t2 = time.perf_counter(); np.matmul(A, B); t3 = time.perf_counter()
    print(f"{n:>5} {'--':>10} {t3-t2:>10.4f} {'--':>8}")
