import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis
import yfinance as yf

def black_scholes_error():
    """
    Compares Monte Carlo pricing with Black-Scholes price and shows convergence as the number of simulations increases.
    """

    errors = []
    sims = np.array([50, 100, 200, 500, 1000, 2000, 5000, 10000])

    # Calculate error in Monte Carlo pricing for various numbers of simulations.
    for sim in sims:
        error = abs(monte_carlo_call_price(n_paths = sim) - black_scholes_price())
        errors.append(error)

    # Plot error against simulations.
    plt.scatter(y=errors, x=sims, label="Absolute Error")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of Monte Carlo simulations (log scale)")
    plt.ylabel("Absolute Error (log scale)")
    plt.title("Monte Carlo convergence to Black-Scholes price")

    # Show expected theoretical convergence.
    reference = errors[0] * (sims[0] / sims) ** 0.5
    plt.plot(sims, reference, linestyle='--', label="O(1/sqrt(N)) reference")

    plt.legend()
    plt.show()

def parameter_sensitivity():
    """
    Shows how option price varies with:
    Volatility (sigma)
    Time to maturity (T)
    Strike price (K)
    """

    # Define ranges for parameters.
    sigma_range = np.linspace(0.1,0.5,50)
    T_range = np.linspace(0.1,2,50)
    K_range = np.linspace(0.5,1.5,50)

    # Calculate Black-Scholes option pricing for given parameters.
    sigma_values = [black_scholes_price(sigma=s) for s in sigma_range]
    T_values = [black_scholes_price(T=t) for t in T_range]
    K_values = [black_scholes_price(K=k) for k in K_range]

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))

    # Plot volatility against option price.
    ax[0].plot(sigma_range, sigma_values)
    ax[0].set_title("Option Price vs Volatility")
    ax[0].set_xlabel("Volatility (σ)")
    ax[0].set_ylabel("Price")

    # Plot time to maturity against option price.
    ax[1].plot(T_range, T_values)
    ax[1].set_title("Option Price vs Time to Maturity")
    ax[1].set_xlabel("Time (T)")

    # Plot strike price against option price.
    ax[2].plot(K_range, K_values)
    ax[2].set_title("Option Price vs Strike Price")
    ax[2].set_xlabel("Strike (K)")

    plt.tight_layout()
    plt.show()

def financial_check():
    """
    Compares empirical log returns to a normal distribution, testing a key assumption of Black-Scholes.
    """

    # Calculate log returns of returns.
    data = yf.download("AAPL", start="2000-01-01", auto_adjust=False)
    price = data["Adj Close"].squeeze()
    log_returns = np.log(price / price.shift(1)).dropna()

    # Calculate measurements to compare against the normal distribution.
    mean = log_returns.mean()
    std = log_returns.std()
    skewness = skew(log_returns)
    kurt = kurtosis(log_returns, fisher=False)

    print(f"Mean: {mean:.6f}")
    print(f"Std Dev: {std:.6f}")
    print(f"Skewness: {skewness:.4f}")
    print(f"Kurtosis: {kurt:.4f} (Normal = 3)")

    # Plot log returns and normal distribution.
    plt.hist(log_returns, bins=50, density=True, alpha=0.6, label="Empirical Returns")

    x = np.linspace(log_returns.min(), log_returns.max(), 1000)
    pdf = norm.pdf(x, mean, std)

    plt.plot(x, pdf, lw=2, label="Fitted Normal")
    plt.title("Log Return Distribution vs Normal Distribution")
    plt.xlabel("Log Returns")
    plt.ylabel("Density")

    plt.legend()
    plt.show()



