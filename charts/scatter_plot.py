import matplotlib.pyplot as plt
import numpy as np

# A scatter plot in Python is a type of plot used to represent the relationship between two variables. 
# Each point in the scatter plot represents a pair of values from the data, allowing you to visualize trends,
# correlations, or patterns in the dataset.

# Generate random data for the scatter plot
x = np.random.rand(50)
 # Linear relationship with some noise
y = 2 * x + 1 + 0.1 * np.random.randn(50)

# Create the scatter plot
plt.scatter(x, y)
# Add titles and axis labels
plt.title('Scatter Plot')
 # Label for the x-axis
plt.xlabel('X-axis')
# Label for the y-axis
plt.ylabel('Y-axis')
# Display the plot
plt.show()