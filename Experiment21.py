import pandas as pd

df = pd.DataFrame({'Text':['Hello','World','Python']})
df['Text'] = df['Text'].str.swapcase()
print(df)
