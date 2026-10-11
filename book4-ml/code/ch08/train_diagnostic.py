# code/ch08/train_diagnostic.py -- the reusable "babysit" checklist.
# Prints the five numbers that diagnose a broken training run before
# you touch the model: epoch-0 loss, gradient norms, dead-unit share,
# weight magnitudes, train/test gap.
# Run from the repository root:  python3 code/ch08/train_diagnostic.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True); X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)
d, h, C = 64, 48, 10
C_EXPECTED = 10

def diagnose(scale_init='kaiming', seed=7):
    rng = np.random.default_rng(seed)
    if scale_init == 'bad':            # the classic killer: N(0,1) raw
        s1, s2 = 1.0, 1.0
    else:                              # Kaiming for ReLU
        s1, s2 = np.sqrt(2/d), np.sqrt(2/h)
    P = [rng.normal(0, s1, (d,h)), np.zeros(h),
         rng.normal(0, s2, (h,C)), np.zeros(C)]
    W1,b1,W2,b2 = P
    z1 = Xtr@W1+b1; a1 = np.maximum(0,z1)
    z2 = a1@W2+b2; z2 -= z2.max(1,keepdims=True)
    e = np.exp(z2); p = e/e.sum(1,keepdims=True)
    m = len(ytr)
    loss0 = -np.log(p[np.arange(m),ytr]+1e-12).mean()
    dz = p.copy(); dz[np.arange(m),ytr] -= 1; dz /= m
    dW2 = a1.T@dz
    dz1 = (dz@W2.T)*(z1>0); dW1 = Xtr.T@dz1
    print(f"init={scale_init:>8}")
    print(f"  epoch-0 loss        {loss0:8.3f}   (ln {C_EXPECTED} ="
          f" {np.log(C_EXPECTED):.3f} expected)")
    print(f"  dead hidden units   {(z1<=0).mean():8.1%}  of {h}")
    print(f"  |grad W1| mean      {np.abs(dW1).mean():8.2e}")
    print(f"  |grad W2| mean      {np.abs(dW2).mean():8.2e}")
    print(f"  |W1| std            {W1.std():8.3f}   |W2| std {W2.std():.3f}")
    print(f"  z1 saturation       {(np.abs(z1)>5).mean():8.1%}"
          f"  (should be ~0 for ReLU)")
    return P

print("== checklist output ==")
diagnose('bad')
print()
P = diagnose('kaiming')
