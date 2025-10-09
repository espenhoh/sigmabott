import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("BTC-USD", period="1mo", interval="1h")
print(data.head())
data["Close"].plot(title="BTC/USDT - siste måned")
plt.show()
