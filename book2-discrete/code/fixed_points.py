"""fixed_points.py -- E[fixed points of a random permutation] = 1.

Theory: X = sum_i 1{sigma(i)=i}; by linearity E[X] = n * 1/n = 1.
No independence needed -- the indicators are far from independent.
Monte Carlo with 10000 trials vs the exact value.
"""
import random


def main():
    random.seed(11)
    n, trials = 6, 10000
    total = 0
    for _ in range(trials):
        p = list(range(n))
        random.shuffle(p)
        total += sum(p[i] == i for i in range(n))
    est = total / trials
    print(f"permutations of n = {n}, {trials} Monte Carlo trials")
    print(f"estimated E[fixed points] = {est:.4f}")
    print(f"exact value               = 1 (n * 1/n, linearity of expectation)")
    print(f"relative error            = {abs(est - 1):.2%}")


if __name__ == "__main__":
    main()
