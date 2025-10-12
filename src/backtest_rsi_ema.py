import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from utils.yahoo_finance import download_yf

# Hent data
data = download_yf("BTC-USD", period="6mo", interval="4h")
print(data.columns)
#if isinstance(data.columns, pd.MultiIndex):
#    data.columns = data.columns.get_level_values(0)

# Indikatorer
data["EMA20"] = EMAIndicator(data.Close, window=20).ema_indicator()
data["RSI"] = RSIIndicator(data["Close"], window=14).rsi()

# Handelsregel
data["signal"] = 0
data.loc[(data["RSI"] < 30) & (data["Close"] > data["EMA20"]), "signal"] = 1     # kjøp
data.loc[(data["RSI"] > 70) & (data["Close"] < data["EMA20"]), "signal"] = -1    # selg

# Beregn avkastning
data["return"] = data["Close"].pct_change()
data["strategy_return"] = data["signal"].shift(1) * data["return"]

# Kumulativ avkastning
data["cum_price"] = (1 + data["return"]).cumprod()
data["cum_strategy"] = (1 + data["strategy_return"]).cumprod()

# Plot
plt.figure(figsize=(10,5))
plt.plot(data.index, data["cum_price"], label="Kjøp & hold")
plt.plot(data.index, data["cum_strategy"], label="Strategi")
plt.legend()
plt.title("RSI+EMA Backtest")
plt.show()

# Enkel statistikk
total_ret = data["cum_strategy"].iloc[-1] - 1
max_dd = (data["cum_strategy"]/data["cum_strategy"].cummax() - 1).min()
print(f"Total avkastning: {total_ret:.2%} | Max drawdown: {max_dd:.2%}")