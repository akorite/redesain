import numpy as np
import time
np.set_printoptions(precision=4, suppress=True)

A = np.array([[1., 1.], [1., 0.]])
w, V = np.linalg.eig(A)
print("eigenvalues of [[1,1],[1,0]]:", np.sort(w))  # phi, -1/phi
phi, psi = (1 + np.sqrt(5)) / 2, (1 - np.sqrt(5)) / 2

def fib_closed(n):          # Binet via diagonalisation
    return int(round((phi**n - psi**n) / np.sqrt(5)))

def fib_rec(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

GOOD = [n for n in range(1, 100) if fib_closed(n) == fib_rec(n)]
print("closed form exact through n =", GOOD[-1],
      "; float64 Binet breaks at n =", GOOD[-1] + 1)
for n in [10, 20, 30, 60, 70]:
    assert fib_closed(n) == fib_rec(n), n
print("closed form == recursion for n in {10,20,30,60,70}: OK")

t0 = time.perf_counter()
for n in range(1, 70):
    fib_closed(n)
t1 = time.perf_counter()
for n in range(1, 70):
    fib_rec(n)
t2 = time.perf_counter()
print(f"closed-form all n<70: {1e3*(t1-t0):.3f} ms")
print(f"recursion   all n<70: {1e3*(t2-t1):.3f} ms")
# exact past the float wall: integer matrix power
Aint = np.array([[1, 1], [1, 0]], dtype=object)
Ai = np.linalg.matrix_power(Aint, 100)
print("F_101 via integer matrix power:", Ai[0, 0])
n = 10
An = np.linalg.matrix_power(A, n)
print(f"A^{n} =")
print(An.astype(int), f"(entries F11={int(An[0,0])}, F10={int(An[1,0])})")
