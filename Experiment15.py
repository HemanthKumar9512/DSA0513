import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,np.nan,np.nan],
                   'B':[np.nan,2,np.nan],
                   'C':[3,np.nan,5]})

result = df[df.isnull().sum(axis=1) >= 2]

print(result)
