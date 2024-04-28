import matplotlib.pyplot as plt
import numpy as np

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
