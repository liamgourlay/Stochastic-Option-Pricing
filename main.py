from monte_carlo import monte_carlo_call_price
from black_scholes import black_scholes_price
from analysis import black_scholes_error, parameter_sensitivity, financial_check
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis
import yfinance as yf

if __name__ == "__main__":
    print("Convergence Analysis (Monte Carlo): Showing how error decreases as the number of simulations increases")
    black_scholes_error()
  
    print("Parameter Sensitivity: Exploring how option price changes with sigma, T, and K")
    parameter_sensitivity()
  
    print("Real Market Data Analysis: Comparing empirical returns to normal distribution")
    financial_check()
