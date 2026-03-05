import pandas as pd

data = {'Region':['East','East','West','West'],
        'Manager':['A','A','B','B'],
        'Salesman':['John','Mary','Tom','Sam'],
        'Sales':[1000,1200,900,1100]}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Sales',
                       index=['Region','Manager','Salesman'],
                       aggfunc='sum')

print(pivot)
