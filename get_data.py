import yfinance as yf

tickers = [
    "AAPL",  # Apple
    "MSFT",  # Microsoft
    "NVDA",  # Nvidia
    "JPM",   # JPMorgan Chase
    "V",     # Visa
    "AMZN",  # Amazon
    "META",  # Meta Platforms
    "JNJ",   # Johnson & Johnson
    "PFE",   # Pfizer
    "XOM",   # ExxonMobil
    "CVX",   # Chevron
    "CAT",   # Caterpillar
    "KO",    # Coca-Cola
    "PG",    # Procter & Gamble
    "GOOGL"  # Alphabet (Google)
]

start = '2014-01-01'
end = '2025-01-01'
start_year = start[0:5]
end_year = end[0:5]

complete_data = yf.download(tickers, start=start, end=end)  # Meta IPO 2012

# Check what columns exist
print(complete_data.columns.levels[0])

# Use "Close" instead of "Adj Close"
if 'Adj Close' in complete_data.columns.levels[0]:
    target_price_data = complete_data['Adj Close']
else:
    target_price_data = complete_data['Close']

target_price_data.to_csv(f"stocks_close_{start_year}_{end_year}.csv")

print("✅ Saved closing prices:", target_price_data.shape)

