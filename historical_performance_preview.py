import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('stocks_close_2015_2025.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set Date as index
df.set_index('Date', inplace=True)

# Calculate percentage returns (normalized to start at 0% from first date)
df_pct = (df / df.iloc[0] - 1) * 100

# Define explicit colors for each stock
colors = {
    'AAPL': '#1f77b4',    # blue
    'AMZN': '#ff7f0e',    # orange
    'CAT': '#2ca02c',     # green
    'CVX': '#d62728',     # red
    'GOOGL': '#9467bd',   # purple
    'JNJ': '#8c564b',     # brown
    'JPM': '#e377c2',     # pink
    'KO': '#7f7f7f',      # gray
    'META': '#bcbd22',    # olive
    'MSFT': '#17becf',    # cyan
    'NVDA': '#ff0000',    # bright red
    'PFE': '#00ff00',     # bright green
    'PG': '#0000ff',      # bright blue
    'V': '#ffff00',       # yellow
    'XOM': '#ff00ff'      # magenta
}

# Figure 1: All stocks including NVDA
plt.figure(1, figsize=(14, 8))

# Sort columns by final return value (highest to lowest)
sorted_columns = df_pct.iloc[-1].sort_values(ascending=False).index

for column in sorted_columns:
    plt.plot(df_pct.index, df_pct[column], label=column, 
             color=colors[column], linewidth=1.5)

plt.title('Historical Stock Returns - All Stocks (2015-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Percentage Return (%)', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Figure 2: All stocks excluding NVDA
plt.figure(2, figsize=(14, 8))
df_pct_no_nvda = df_pct.drop('NVDA', axis=1)

# Sort columns by final return value (highest to lowest)
sorted_columns_no_nvda = df_pct_no_nvda.iloc[-1].sort_values(ascending=False).index

for column in sorted_columns_no_nvda:
    plt.plot(df_pct_no_nvda.index, df_pct_no_nvda[column], label=column,
             color=colors[column], linewidth=1.5)

plt.title('Historical Stock Returns - Excluding NVDA (2015-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Percentage Return (%)', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Show both plots
plt.show()