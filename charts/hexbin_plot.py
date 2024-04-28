import numpy as np
import matplotlib.pyplot as plt

# A hexbin plot is a type of plot used in data visualization to display the relationship between two continuous variables.
# It's useful when dealing with large datasets or when you want to understand the density of points in a 2D space. 
# In Python, you can create hexbin plots using Matplotlib or Seaborn.

# Generate random data
np.random.seed(0)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)

# Create a hexbin plot
plt.figure(figsize=(8, 6))
hexbin_plot = plt.hexbin(x, y, gridsize=30, cmap='viridis', reduce_C_function=np.mean)

# Add a colorbar to indicate density
plt.colorbar(hexbin_plot, label='Density')

# Add titles and labels
plt.title("Hexbin Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Display the plot
plt.show()
