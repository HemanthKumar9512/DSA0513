import pandas as pd

data = {'Item':['Pen','Pen','Pencil','Pencil'],
        'Sales':[100,200,150,120]}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Sales', index='Item',
                       aggfunc=['max','min'])

print(pivot)
