import numpy as np
import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define a function Z = f(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a contour plot
plt.figure(figsize=(8, 6))
contour_plot = plt.contour(X, Y, Z, levels=20, cmap='viridis')  # Adjust levels for desired granularity

# Add contour labels
plt.clabel(contour_plot, inline=True, fontsize=8)

# Add titles and labels
plt.title("Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Display the plot
plt.show()
