import pandas as pd

data = {
    'job_id': [101, 102, 103, 104],
    'job_title': ['Manager', 'Analyst', 'Clerk', 'Developer'],
    'salary': [60000, 45000, 30000, 70000]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by='job_title', ascending=False)

print(sorted_df)
