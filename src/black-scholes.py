import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis
import yfinance as yf

def black_scholes_price(S0=1.0, K=1.1, r=0.1, sigma=0.2, T=0.5):
    """
    Computes the Black-Scholes price of a European call option.

    Parameters
    ----------
    S0: float
        Initial asset price
    K: float
        Strike price
    T: float
        Time till option activates
    r: float
        Risk-free interest rate
    sigma: float
        Volatility

    Returns
    ----------
    float
        Call option price
    """
    if T<= 0:
        return max(S0-K, 0)

    # Compute d1 and d2
    d1 = (np.log(S0 / K) + (r + (1 / 2) * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Evaluate standard normal CDF
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)

    # Calculate Black-Scholes call price.
    call_price = S0 * Nd1 - K * np.exp(-r * T) * Nd2

    return call_price
