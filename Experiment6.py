import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock.csv")

plt.scatter(df['Close'], df['Volume'])
plt.xlabel("Stock Price")
plt.ylabel("Volume")
plt.show()
