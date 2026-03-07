import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,2,np.nan],
                   'B':[4,np.nan,6]})

df = df.fillna(0)

print(df)
