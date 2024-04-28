import numpy as np
import matplotlib.pyplot as plt

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
