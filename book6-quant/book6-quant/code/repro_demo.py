import numpy as np
def run(seed):
    rng=np.random.default_rng(seed)
    r=rng.normal(0.0008,0.02,720)
    return r.mean()*252, r.std()*np.sqrt(252)
for s in (7,7,99):
    m,sd=run(s)
    print(f"seed {s}: ann ret {m:+.1%}  vol {sd:.1%}")
print("same seed -> same numbers; pin the seed, pin the data, pin the code")
