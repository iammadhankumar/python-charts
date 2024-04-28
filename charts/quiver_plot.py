import matplotlib.pyplot as plt
import numpy as np

# A quiver plot in Python is used to display vector fields or directional data. 
# It represents vectors with arrows, where each arrow has a specific direction and magnitude. 
# Quiver plots are often used to visualize vector fields, wind directions, electromagnetic fields, gradients, 
# or other data with directional components.

# Create a grid of x and y coordinates
x = np.linspace(0, 2 * np.pi, 10)
y = np.linspace(0, 2 * np.pi, 10)
X, Y = np.meshgrid(x, y)

# Define the vector field (U, V) based on functions of X and Y
U = np.cos(X)  # x-component of the vector field
V = np.sin(Y)  # y-component of the vector field

# Create a quiver plot
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color='b', angles='xy', scale_units='xy', scale=1)

# Add titles and labels
plt.title("Quiver Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
