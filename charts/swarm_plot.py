import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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
