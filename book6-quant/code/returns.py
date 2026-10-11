"""returns.py -- simple vs log returns and annualisation (ch01).

Every quantity in the book is computed the way this file does it:
a price series P_t gives a simple net return R_t = P_t/P_{t-1} - 1
and a log return r_t = log(P_t/P_{t-1}) = log(1 + R_t).
"""
import numpy as np


def simple_returns(p):
    p = np.asarray(p, dtype=float)
    return p[1:] / p[:-1] - 1.0


def log_returns(p):
    p = np.asarray(p, dtype=float)
    return np.log(p[1:] / p[:-1])


def annualise_mean(daily_mean, periods_per_year):
    """Mean return annualised additively in log space (the correct way:
    log returns add, so a sum of 365 daily log returns has mean
    365 * daily mean)."""
    return daily_mean * periods_per_year


def annualise_vol(daily_vol, periods_per_year):
    """Volatility annualises by the square-root rule: a sum of n
    independent returns has std sqrt(n) * sigma."""
    return daily_vol * np.sqrt(periods_per_year)


if __name__ == "__main__":
    p = [100.0, 102.0, 101.0, 105.0]
    R = simple_returns(p)
    r = log_returns(p)
    print("P     =", p)
    print("R     =", np.round(R, 6))
    print("r     =", np.round(r, 6))
    # telescoping: the sum of log returns is the log of the total ratio
    print("sum(r)      =", round(r.sum(), 6))
    print("log(P4/P1)  =", round(np.log(p[-1] / p[0]), 6))
    # no such identity for simple returns
    print("prod(1+R)-1 =", round(np.prod(1.0 + R) - 1.0, 6))
