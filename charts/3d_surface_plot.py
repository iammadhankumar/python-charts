import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plotting

# A 3D surface plot in Python allows you to visualize a three-dimensional dataset on a 2D plane with the addition of a third dimension for height or depth. 
# Surface plots are useful for visualizing functions of two variables, terrain data, or other 3D data.

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define a function for Z based on X and Y
Z = np.sin(np.sqrt(X**2 + Y**2))  # Example function

# Create a 3D surface plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Add a colorbar to indicate height or value
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label='Height')

# Add titles and labels
ax.set_title("3D Surface Plot Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Display the plot
plt.show()
