import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

data = yf.download("BTC-USD", period="1mo", interval="1h", group_by="column", progress=False)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)
data = data.dropna().copy()
close = pd.to_numeric(data["Close"], errors="coerce")

ema20 = EMAIndicator(close, window=20).ema_indicator()
rsi = RSIIndicator(close, window=14).rsi()

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(11, 6))

ax1.plot(data.index, close, label="Close", linewidth=1)
ax1.plot(data.index, ema20, label="EMA20", linewidth=1)
ax1.legend()
ax1.set_title("BTC-USD + EMA20")

ax2.plot(data.index, rsi, label="RSI(14)", linewidth=1)
ax2.axhline(70, linestyle="--")
ax2.axhline(30, linestyle="--")
ax2.legend()
ax2.set_title("RSI")

plt.tight_layout()
plt.show()
