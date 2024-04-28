import matplotlib.pyplot as plt
import numpy as np

# A bubble chart in Python is a scatter plot where each point's size is determined by a third variable, 
# creating a visual representation of additional information. Bubble charts are helpful in showing relationships between three variables. 
# You can create bubble charts in Python with libraries like Matplotlib, Seaborn, or Plotly.

# Generate random data
np.random.seed(0)
x = np.random.rand(50) * 100  # X-axis values
y = np.random.rand(50) * 100  # Y-axis values
sizes = np.random.rand(50) * 1000  # Bubble sizes
colors = np.random.rand(50) * 100  # Colors for each bubble

# Create a bubble chart
plt.figure(figsize=(8, 6))
bubble_plot = plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')

# Add a colorbar to indicate color meaning
plt.colorbar(bubble_plot, label='Color scale')

# Add titles and labels
plt.title("Bubble Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
