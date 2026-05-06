import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis
import yfinance as yf

def monte_carlo_call_price(S0=1.0, K = 1.1, T = 0.5, r = 0.1, sigma = 0.2,
                            steps = 1000, n_paths = 1000, seed = 42):
    """
    Price a European call option using Monte Carlo simulation under Geometric Brownian Motion.

    Parameters
    ----------
    S0: float
        Initial asset price
    K: float
        Strike price
    T: float
        Time to maturity
    r: float
        Risk-free interest rate
    sigma: float
        Volatility
    steps: int
        Number of time steps per path
    n_paths: int
        Number of Monte Carlo simulations
    seed: int
        Random seed for reproducibility

    Returns
    ----------
    float
        Estimated call option price
    """

    np.random.seed(seed)

    dt = T / steps

    # Generate standard normal random variables.
    Z = np.random.normal(0, 1, (n_paths, steps))

    # Log-price increments.
    drift = (r - 0.5 * sigma ** 2) * dt
    diffusion = sigma * np.sqrt(dt) * Z
    log_increments = drift + diffusion

    # Log-price paths.
    log_paths = np.cumsum(log_increments, axis = 1)

    # Price paths.
    S_paths = S0 * np.exp(log_paths)
    S_paths = np.hstack([np.full((n_paths, 1) ,S0), S_paths])

    # Calculate discounted expected payoffs.
    payoffs = [max(element - K, 0) for element in S_paths[:, -1]]
    price = np.exp(-r * T) * np.mean(payoffs)

    return price
