import pandas as pd

df = pd.DataFrame({'Name':['India','Canada','Finland']})

result = df['Name'].str.find('an')

print(result)
