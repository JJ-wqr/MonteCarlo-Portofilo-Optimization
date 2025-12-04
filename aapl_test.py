import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = yf.download("AAPL", start="2014-01-01", end="2024-01-01")
prices = data["Close"]

returns = np.log(prices / prices.shift(1)).dropna()


# mu = returns.mean()
# mu = float(mu.iloc[0])
# sigma = returns.std()
# sigma = float(sigma.iloc[0])

mu = returns.mean()          # already a float
sigma = returns.std()  

print(mu)


num_sim = 100       # number of simulations
num_days = 252       # 1 year of trading days
last_price = float(prices.iloc[-1])

simulations = np.zeros((num_days, num_sim))

for s in range(num_sim):
    price = last_price
    for t in range(num_days):
        shock = sigma * np.random.normal()
        drift = (mu - 0.5 * sigma**2)
        
        price = price * np.exp(drift + shock)
        simulations[t, s] = price

final_prices = simulations[-1, :]
mean_final = final_prices.mean()
var_95 = np.percentile(final_prices, 5)


# Printing Expected return
returns_simulated = (final_prices - last_price) / last_price

expected_return = returns_simulated.mean()
print("Expected return", expected_return)



plt.plot(simulations)
plt.title("Monte Carlo Simulation")
plt.xlabel("Days into the Future")
plt.ylabel("Simulated Stock Price (USD)")
plt.title("Monte Carlo Simulation: AAPL")
plt.show()

