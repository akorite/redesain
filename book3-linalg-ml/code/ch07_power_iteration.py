import numpy as np
np.set_printoptions(precision=6, suppress=True)

# power iteration on a symmetric matrix: converge to dominant eigenpair
A = np.array([[2., 1., 0.], [1., 2., 1.], [0., 1., 2.]])
x = np.array([1., 0.5, -0.25])
print("A =")
print(A)
for k in range(8):
    x = A @ x
    lam = x[np.argmax(np.abs(x))]  # Rayleigh-ish: largest component ratio
    x = x / np.linalg.norm(x)
    rq = x @ A @ x
    print(f"k={k+1}: lambda~{rq:.6f}  x={x}")
w, V = np.linalg.eig(A)
print("true dominant:", np.abs(w).max(), " eigenvector:", V[:, np.argmax(np.abs(w))])
