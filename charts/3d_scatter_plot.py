import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# A 3D scatter plot in Python allows you to visualize a dataset with three dimensions. This type of plot is useful when you want to understand 
# the relationships between three different variables or observe clusters and patterns in a 3D space.

# Generate random data for 3D scatter plot
np.random.seed(0)
x = np.random.randn(100)  # X-axis values
y = np.random.randn(100)  # Y-axis values
z = np.random.randn(100)  # Z-axis values

# Create a 3D scatter plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

# Plot the scatter points
scatter = ax.scatter(x, y, z, c='b', marker='o', alpha=0.7, s=50)  # Adjust color, marker, size, and transparency

# Add titles and labels
ax.set_title("3D Scatter Plot Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Set the view angle for better visualization
ax.view_init(elev=20, azim=30)  # Adjust elevation and azimuth for a clear view

# Display the plot
plt.show()
