import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock.csv")
df['Date'] = pd.to_datetime(df['Date'])

data = df[(df['Date'] >= '2020-01-01') & (df['Date'] <= '2020-01-10')]

data.plot(x='Date', y='Volume', kind='bar')
plt.show()
