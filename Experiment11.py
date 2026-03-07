import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))

df.iloc[2,1] = np.nan
df.iloc[5,3] = np.nan

def highlight_nan(val):
    return 'background-color: red' if pd.isna(val) else ''

df.style.applymap(highlight_nan)
