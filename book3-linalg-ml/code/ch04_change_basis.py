import numpy as np
np.set_printoptions(precision=4, suppress=True)

# T = quarter-turn:  standard matrix A
A = np.array([[0., -1.], [1., 0.]])

# new basis B = {b1, b2} = columns of B
B = np.array([[2., 1.], [1., 1.]])      # b1=(2,1), b2=(1,1)

# same map in B-coordinates:  [T]_B = B^{-1} A B
TB = np.linalg.inv(B) @ A @ B
print("[T]_B =")
print(TB)

# check on a vector: v = (5, 1) standard.
v = np.array([5., 1.])
c = np.linalg.solve(B, v)             # [v]_B : B-coords of v
Tv_A = A @ v                          # [T(v)] in standard coords
Tv_B = B @ (TB @ c)                   # via B-coords
print("[v]_B =", c)
print("via A:", Tv_A)
print("via [T]_B:", Tv_B)
print("same physical answer:", np.allclose(Tv_A, Tv_B))
print("A = B [T]_B B^-1 ok:",
      np.allclose(A, B @ TB @ np.linalg.inv(B)))
