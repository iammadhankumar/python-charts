import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# A swarm plot in Python is a type of scatter plot that displays categorical data, showing the distribution of data points 
# along a categorical axis while avoiding overlap. This plot is useful for visualizing the spread of data in a way that 
# each point is visible without overlaps, often used in conjunction with box plots or violin plots for more detailed insights.
# If needed, install Seaborn
# pip install seaborn

# Sample data for the swarm plot
np.random.seed(0)
categories = ['Category A', 'Category B', 'Category C']
values = [np.random.randn(50) + i for i in range(3)]  # Create 50 random values for each category

# Create a DataFrame for Seaborn
import pandas as pd
df = pd.DataFrame({
    'Category': np.repeat(categories, 50),  # Repeat each category 50 times
    'Value': np.concatenate(values)  # Concatenate the random values
})

# Create a swarm plot
plt.figure(figsize=(10, 6))
sns.swarmplot(x='Category', y='Value', data=df, size=6, color='dodgerblue')

# Add titles and labels
plt.title("Swarm Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")

# Display the plot
plt.show()
