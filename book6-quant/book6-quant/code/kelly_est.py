import numpy as np
# f* = mu/sig^2 for continuous approx; sensitivity to estimation error
mu_t, sig_t = 0.10, 0.20
f_t = mu_t/sig_t**2
print(f"true: mu={mu_t} sig={sig_t}  f*={f_t:.2f}")
for dm in (-0.5,-0.25,0,0.25,0.5):
    mu_h=mu_t*(1+dm); f_h=mu_h/sig_t**2
    print(f"mu off {dm:+.0%}:  fhat={f_h:+.2f}  sizing error {f_h/f_t:+.2f}x")
print("edge halves -> f* halves; bet size carries the whole estimation error")
