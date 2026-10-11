import numpy as np
np.set_printoptions(precision=4, suppress=True)

# synthetic "image": smooth blob + sharp edge + noise, 64x64
rng = np.random.default_rng(5)
y, x = np.mgrid[0:64, 0:64]
img = np.exp(-((x-32)**2 + (y-24)**2) / 300.) + (x > 40).astype(float)
img += 0.02 * rng.standard_normal(img.shape)
U, S, Vt = np.linalg.svd(img)
print("image shape:", img.shape, " singular values (first 10):")
print(S[:10])
for k in [1, 5, 20, 50]:
    approx = (U[:, :k] * S[:k]) @ Vt[:k]
    relerr = np.linalg.norm(img - approx) / np.linalg.norm(img)
    kept = 2 * k * 64 + k          # numbers stored vs 64*64
    print(f"k={k:2d}: rel-err {relerr:.4f}  stored {kept:5d}/{64*64} "
          f"({100*kept/(64*64):4.1f}%)")
