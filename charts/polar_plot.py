import matplotlib.pyplot as plt
import numpy as np

# A polar plot in Python is used to represent data in a polar coordinate system, where each point is defined by a radius and an angle. 
# Polar plots are useful for showing directional data or data that is best represented in a circular format, such as wind direction or radar charts.

# Define the angle values (theta) and the radius values (r)
theta = np.linspace(0, 2 * np.pi, 100)  # Angles from 0 to 2π (circle)
r = np.abs(np.sin(theta))  # Radius based on a sine function

# Create a polar plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)  # Create a polar subplot

ax.plot(theta, r, label="|sin(θ)|")  # Plot a line on the polar chart

# Add titles and labels
ax.set_title("Polar Plot Example", va='bottom')

# Add a legend
ax.legend()

# Display the plot
plt.show()
