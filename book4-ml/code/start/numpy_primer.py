# The same ideas on whole arrays at once (Book 4, Chapter 1 does this in depth).
import numpy as np

X = np.array([[1.0, 2.0],
              [3.0, 4.0],
              [5.0, 6.0]])            # 3 samples (rows), 2 features (columns)
w = np.array([10.0, 1.0])             # one weight per feature

print("shape of X:", X.shape)
print("X @ w     :", X @ w)           # one prediction per row
print("column means:", X.mean(axis=0))
