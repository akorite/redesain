"""ch02: three canonical time series + a cointegrated pair.
Every path is seeded so printed outputs reproduce exactly."""
import numpy as np

def white_noise(T=500, sigma=1.0, seed=3):
    return np.random.default_rng(seed).normal(0.0, sigma, T)

def ar1(T=500, phi=0.85, sigma=1.0, seed=3):
    e = np.random.default_rng(seed).normal(0.0, sigma, T)
    x = np.zeros(T)
    for t in range(1, T):
        x[t] = phi * x[t-1] + e[t]
    return x

def random_walk(T=500, sigma=1.0, seed=3):
    return np.cumsum(np.random.default_rng(seed).normal(0.0, sigma, T))

def ou(T=500, mu=4.0, theta=0.12, sigma=0.35, x0=None, seed=9):
    """Ornstein-Uhlenbeck: dx = theta(mu - x)dt + sigma dW."""
    e = np.random.default_rng(seed).normal(0.0, sigma, T)
    x = np.zeros(T)
    x[0] = mu if x0 is None else x0
    for t in range(1, T):
        x[t] = x[t-1] + theta * (mu - x[t-1]) + e[t]
    return x

def coint_pair(T=500, beta=2.0, theta=0.10, seed=21):
    """y_t = beta*x_t + z_t, x random walk, z OU -> spread mean-reverts."""
    x = random_walk(T, sigma=0.8, seed=seed)
    z = ou(T, mu=0.0, theta=theta, sigma=0.3, seed=seed+1)
    return x, beta * x + z, z

if __name__ == "__main__":
    T = 500
    wn, a1, o, rw = white_noise(T), ar1(T), ou(T), random_walk(T)
    print(f"white noise : mean={wn.mean():+.3f} sd={wn.std():.3f} "
          f"first50 sd={wn[:50].std():.3f} last50 sd={wn[-50:].std():.3f}")
    print(f"AR(1) phi.85: mean={a1.mean():+.3f} sd={a1.std():.3f}")
    print(f"random walk : mean={rw.mean():+.3f} sd={rw.std():.3f} "
          f"start={rw[0]:+.2f} end={rw[-1]:+.2f} (level wanders)")
    print(f"OU theta.12 : mean={o.mean():+.3f} sd={o.std():.3f} "
          f"-> pulls to mu=4.00, half-life {np.log(2)/0.12:.1f} bars")
    x, y, z = coint_pair(T)
    print(f"coint pair  : y=2x+z, spread z mean={z.mean():+.3f} "
          f"sd={z.std():.3f} (x sd {x.std():.2f}, y sd {y.std():.2f})")
