# Monte Carlo Option Pricing & Black–Scholes Validation

This project implements Monte Carlo simulation for pricing European call options under Geometric Brownian Motion. It includes comparison against the analytical Black–Scholes solution, convergence analysis, parameter sensitivity, and empirical validation of model assumptions using real market data.

---

# Strategy Overview

The strategy:

- Assumes asset prices follow Geometric Brownian Motion
- Simulates price paths using Brownian motion
- Prices options via discounted expected payoff
- Benchmarks results against the Black–Scholes equation for option prices
- Tests the convergence of Monte Carlo estimates
- Analyses sensitivity to key parameters (σ, T, K)
- Compares real market returns to the normality assumption

---

# Benchmark

Monte Carlo prices are compared against the analytical Black–Scholes price for validation.

---

# Features

- Monte Carlo simulation of price paths
- Black–Scholes analytical pricing
- Convergence analysis
- Parameter sensitivity visualisation
- Empirical return distribution analysis using market data
- Statistical comparison (mean, volatility, skewness, kurtosis)

---

# Results

- Monte Carlo estimates converge to the Black–Scholes price as simulations increase
- Error decay follows the expected: O(1/\sqrt(N))
- Option prices increase with volatility and time to maturity
- Option prices decrease as strike price increases
- Real data leads to the following results:
    Mean: 0.000880
    Std Dev: 0.024982
    Skewness: -3.9217
    Kurtosis: 117.9150 (Normal = 3)

---

# Findings

- Monte Carlo provides an unbiased but slow-converging estimation of option prices
- Convergence behaviour aligns with theoretical expectations
- Black–Scholes assumptions are violated in real data:
- Returns exhibit fat tails (kurtosis > 3)
- Returns exhibit non-zero skewness
- This highlights limitations of constant-volatility models in practice

See:

results/convergence.png
results/sensitivity.png
results/return_distribution.png

---

# How to Run

```bash
pip install -r requirements.txt
python src/main.py
