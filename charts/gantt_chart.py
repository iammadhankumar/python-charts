import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

# Define task data with start and end dates
tasks = {
    'Task 1': {'start': '2024-01-01', 'end': '2024-01-10'},
    'Task 2': {'start': '2024-01-05', 'end': '2024-01-15'},
    'Task 3': {'start': '2024-01-10', 'end': '2024-01-20'},
    'Task 4': {'start': '2024-01-15', 'end': '2024-01-25'}
}

# Convert the task data to a DataFrame and calculate duration
df = pd.DataFrame(tasks).T
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])
df['duration'] = df['end'] - df['start']

# Create a Gantt chart
plt.figure(figsize=(10, 6))
y_ticks = list(range(len(df)))
task_labels = df.index

# Explicitly convert `df['start'].dt.to_pydatetime()` to a numpy array to avoid FutureWarning
start_dates = np.array(df['start'].dt.to_pydatetime())

# Plot the Gantt chart
plt.barh(y_ticks, df['duration'].dt.days, left=start_dates, color='skyblue')

# Add titles and labels
plt.title("Gantt Chart Example")
plt.xlabel("Time")
plt.ylabel("Tasks")
plt.yticks(y_ticks, task_labels)

# Display the plot
plt.show()
