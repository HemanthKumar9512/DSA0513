import pandas as pd

# Read the employee file
df = pd.read_csv('employee.csv')

# Get distinct department IDs
distinct_dept_ids = df['department_id'].unique()

print("Distinct Department IDs:")
print(distinct_dept_ids)

# Alternative: Convert to list
print("\nAs List:")
print(list(distinct_dept_ids))
