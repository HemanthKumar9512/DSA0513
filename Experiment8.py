import pandas as pd

data = {'Item':['Pen','Pen','Pencil','Pencil'],
        'Units':[10,15,20,25]}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Units', index='Item', aggfunc='sum')

print(pivot)
