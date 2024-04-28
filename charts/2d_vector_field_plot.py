import matplotlib.pyplot as plt
import numpy as np

# Create a grid of x and y coordinates
x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)
X, Y = np.meshgrid(x, y)  # Generate a meshgrid for plotting

# Define the vector field (U, V) based on functions of X and Y
U = -Y  # x-component of the vector field
V = X  # y-component of the vector field

# Create a 2D vector field plot
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='b', alpha=0.7)

# Add titles and labels
plt.title("2D Vector Field Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
