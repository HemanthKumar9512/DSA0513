import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

start_date = "2023-01-01"
end_date = "2023-12-31"

data = yf.download("GOOGL", start=start_date, end=end_date)

plt.figure(figsize=(10,5))
plt.plot(data['Close'])
plt.title("Alphabet Inc Stock Prices (2023)")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
