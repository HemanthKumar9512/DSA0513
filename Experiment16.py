import pandas as pd

data = {'school_code':['S1','S1','S2','S2'],
        'name':['John','Mary','Tom','Sam'],
        'age':[15,16,15,14]}

df = pd.DataFrame(data)

group = df.groupby('school_code')

print(type(group))
