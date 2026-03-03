import pandas as pd

# Read the job history file
df = pd.read_csv('job_history.csv')

# Group by employee_id and count distinct jobs
job_counts = df.groupby('employee_id')['job_id'].nunique().reset_index()
job_counts.columns = ['employee_id', 'num_jobs']

# Filter employees with 2 or more jobs
multi_job_employees = job_counts[job_counts['num_jobs'] >= 2]

print("Employees who have done 2 or more jobs:")
print(multi_job_employees)

# Extract just the employee IDs
employee_ids = multi_job_employees['employee_id'].tolist()
print(f"\nEmployee IDs: {employee_ids}")

# Alternative: Show detailed job history for these employees
print("\nDetailed Job History:")
for emp_id in employee_ids:
    emp_history = df[df['employee_id'] == emp_id]
    print(f"\nEmployee {emp_id}:")
    print(emp_history[['job_id', 'start_date', 'end_date']])
