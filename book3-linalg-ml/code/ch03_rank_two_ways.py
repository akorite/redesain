import numpy as np

rng = np.random.default_rng(4)
np.seterr(all="ignore")

def rref_rank(M, tol=1e-10):
    M = M.copy().astype(float)
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        k = np.argmax(np.abs(M[r:, c])) + r
        if abs(M[k, c]) < tol:
            continue
        M[[r, k]] = M[[k, r]]
        M[r] = M[r] / M[r, c]
        for i in range(rows):
            if i != r:
                M[i] -= M[i, c] * M[r]
        r += 1
    return r

print(f"{'shape':>9} {'np rank':>8} {'col rank (pivots)':>18} {'row rank (pivots of A.T)':>24}")
for m, n in [(4, 5), (5, 4), (6, 6)]:
    A = rng.standard_normal((m, n))
    # make A low-rank on purpose: column 3 = column 0 - 2*column 1
    A[:, 3] = A[:, 0] - 2 * A[:, 1]
    print(f"{m}x{n:>6} {np.linalg.matrix_rank(A):>8} "
          f"{rref_rank(A):>18} {rref_rank(A.T):>24}")
