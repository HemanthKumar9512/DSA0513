import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),
                  columns=['A','B','C','D'])

def color(val):
    return 'color:red' if val < 0 else 'color:black'

df.style.applymap(color)
