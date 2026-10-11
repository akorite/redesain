import numpy as np
rng = np.random.default_rng(4)

# die: E=3.5 Var=35/12; binomial n=10 p=0.3: E=3 Var=2.1
dice = rng.integers(1, 7, 200_000)
print("die:      mean %.4f vs 3.5   var %.4f vs %.4f"
      % (dice.mean(), dice.var(), 35/12))
binom = rng.binomial(10, 0.3, 200_000)
print("binomial: mean %.4f vs 3.0   var %.4f vs 2.1"
      % (binom.mean(), binom.var()))
# empirical Bayes check on simulated medical test
N = 1_000_000
sick = rng.random(N) < 0.001
pos = (rng.random(N) < np.where(sick, 0.99, 0.05))
print("P(sick|pos) sim %.4f" % sick[pos].mean())
