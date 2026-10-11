import numpy as np
np.set_printoptions(precision=4, suppress=True)

# A = [[4,1],[2,3]]: by hand, lambda^2 - 7 lambda + 10 = 0 -> lambda = 5, 2
A = np.array([[4., 1.], [2., 3.]])
w_hand, V_hand = 5.0, np.array([1., 1.])
w2_hand, V2_hand = 2.0, np.array([1., -2.])
print("A =")
print(A)
print("hand: lambda=5, v=(1,1):", np.allclose(A @ V_hand, 5 * V_hand))
print("hand: lambda=2, v=(1,-2):", np.allclose(A @ V2_hand, 2 * V2_hand))

w, V = np.linalg.eig(A)
print("np.linalg.eig eigenvalues:", np.sort(w))
print("eig vectors (cols):")
print(V)
print("trace == sum lambda:", np.isclose(np.trace(A), w.sum()))
print("det == prod lambda:", np.isclose(np.linalg.det(A), w.prod()))
