import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plotting

# Data for the 3D bar chart
x = [1, 2, 3, 4, 5]  # x-axis categories
y = [1, 2, 3]  # y-axis categories
xpos, ypos = np.meshgrid(x, y)  # Create a grid of x and y positions
xpos = xpos.flatten()  # Flatten the grid for plotting
ypos = ypos.flatten()  # Flatten the grid for plotting
zpos = np.zeros_like(xpos)  # Base position for bars

# Heights for the bars
z = np.array([1, 2, 3, 4, 5, 2, 3, 1, 4, 3, 2, 5, 4, 3, 2])

# Create a 3D bar chart
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

dx = dy = 0.5  # Width and depth of the bars
ax.bar3d(xpos, ypos, zpos, dx, dy, z, color='skyblue', edgecolor='k', alpha=0.7)

# Add titles and labels
ax.set_title("3D Bar Chart Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Height")

# Set the view angle for better visualization
ax.view_init(elev=20, azim=30)  # Adjust elevation and azimuth

# Display the plot
plt.show()
