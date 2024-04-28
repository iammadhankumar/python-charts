import matplotlib.pyplot as plt
import numpy as np

# A stem plot in Python is used to visualize discrete data points along a line, where each point has a "stem" that connects it to a baseline. 
# It's similar to a bar chart but is more suitable for displaying discrete signals, sparse data, or scatter-like data with emphasis on discrete points.

# Define data points for the x-axis and y-axis
x = np.arange(0, 10, 1)  # From 0 to 9
y = np.sin(x)  # A simple sine wave

# Create a stem plot
plt.figure(figsize=(8, 6))
plt.stem(x, y, linefmt='-', markerfmt='o', basefmt='k-')

# Add titles and labels
plt.title("Stem Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
