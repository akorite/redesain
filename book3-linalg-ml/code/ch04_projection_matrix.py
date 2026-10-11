import numpy as np
np.set_printoptions(precision=4, suppress=True)

# project onto the line spanned by u = (3, 4):  P = u u^T / u^T u
u = np.array([3., 4.])
P = np.outer(u, u) / (u @ u)
print("P =")
print(P)

x = np.array([7., 1.])
Px = P @ x
print("Px =", Px)
print("parallel to u?", np.allclose(Px, (Px @ u) / (u @ u) * u))
print("residual perpendicular?", np.allclose((x - Px) @ Px, 0))
print("P is symmetric:", np.allclose(P, P.T))
print("P^2 = P:", np.allclose(P @ P, P))

# every vector splits into along-u + perpendicular:
print("x = Px + (x-Px):", np.allclose(x, Px + (x - Px)))
