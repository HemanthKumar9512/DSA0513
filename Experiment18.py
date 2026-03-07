import pandas as pd

data = {'school_code':['S1','S1','S2','S2'],
        'class':['10','9','10','9'],
        'name':['John','Mary','Tom','Sam']}

df = pd.DataFrame(data)

group = df.groupby(['school_code','class'])

print(group.size())
