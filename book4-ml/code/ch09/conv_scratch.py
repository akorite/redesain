# code/ch09/conv_scratch.py -- 2-D convolution as four loops,
# verified element-for-element against scipy.signal.correlate2d.
# Then the output-size arithmetic the chapter drills.
# Run from the repository root:  python3 code/ch09/conv_scratch.py
import numpy as np
from scipy.signal import correlate2d   # DL 'conv' = cross-correlation
from sklearn.datasets import load_digits

def conv2d(img, ker):
    """valid-mode 2-D convolution: slide ker over img, dot each patch."""
    H, W = img.shape; k, _ = ker.shape
    out = np.zeros((H - k + 1, W - k + 1))
    for i in range(H - k + 1):
        for j in range(W - k + 1):
            out[i, j] = (img[i:i+k, j:j+k] * ker).sum()
    return out

digits = load_digits()
img = digits.images[17]          # an 8x8 digit
ker = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

ours = conv2d(img, ker)
ref  = correlate2d(img, ker, mode='valid')
print("digit label:", digits.target[17])
print("ours [0,:4] :", np.round(ours[0, :4], 2))
print("scipy [0,:4]:", np.round(ref[0, :4], 2))
print("max abs diff:", np.abs(ours - ref).max())
print("output shape:", ours.shape, "(8-3+1 = 6, matches)")

# --- output-size arithmetic table --------------------------------------
print("\nout = floor((H + 2p - k)/s) + 1:")
for H, k, p, s in [(28, 3, 1, 1), (28, 5, 0, 1), (28, 3, 0, 2),
                   (32, 5, 2, 1), (224, 11, 0, 4), (7, 3, 1, 2)]:
    o = (H + 2*p - k) // s + 1
    print(f"  H={H:>3} k={k:>2} pad={p} stride={s}  ->  out={o}")
