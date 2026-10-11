import numpy as np
np.set_printoptions(precision=6, suppress=True)
np.random.seed(1)

# weather chain: columns are "from", rows are "to" (column-stochastic)
# state 0 = rain, state 1 = sun
P = np.array([[0.9, 0.3],
              [0.1, 0.7]])
print("P =")
print(P)
print("columns sum to 1:", np.allclose(P.sum(axis=0), 1))

w, V = np.linalg.eig(P)
print("eigenvalues:", w)
pi = V[:, np.argmax(w)].real
pi = pi / pi.sum()
print("steady state (eigenvector of lambda=1):", pi)

# matrix powers from a rainy start
x = np.array([1., 0.])
for k in [10, 20, 50, 200]:
    xk = np.linalg.matrix_power(P, k) @ x
    print(f"P^{k} x0 = {xk}")
# Monte Carlo check
rng = np.random.default_rng(0)
state, counts = 0, np.zeros(2)
for _ in range(200000):
    state = rng.choice(2, p=P[:, state])
    counts[state] += 1
print("Monte Carlo fractions:", counts / counts.sum())
