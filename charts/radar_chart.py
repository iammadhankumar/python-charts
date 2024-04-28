import matplotlib.pyplot as plt
import numpy as np

# A radar chart in Python, also known as a spider chart or web chart, is a graphical method of displaying multivariate data in a way that allows for easy comparison across multiple categories. 
# Each axis represents a different category, and the data points are connected to form a polygon. This chart type is commonly used for comparing multiple variables or showing performance across different metrics.

# Define the labels and data for the radar chart
labels = np.array([' A', ' B', ' C', ' D', ' E'])

# Labels for the radar chart axes
data = np.array([4, 5, 3, 4, 2])

# Create angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
# Complete the loop by repeating the first data point
data = np.concatenate((data, [data[0]]))
# Complete the loop by repeating the first angle
angles = np.concatenate((angles, [angles[0]]))

# Plot data points in a polar (circular) chart
plt.polar(angles, data, marker='o')
# Fill the area under the plot with transparency
plt.fill(angles, data, alpha=0.25)
# Add a title to the radar chart
plt.title('Radar Chart')
# Display the plot
plt.show()