import matplotlib.pyplot as plt
import numpy as np

# A histogram in Python is a plot that shows the distribution of a dataset by dividing the data into bins (intervals) and displaying the frequency of data points in each bin. 
# It is useful for visualizing the shape and spread of a dataset, identifying skewness, kurtosis, or outliers, and exploring underlying data patterns.

# Generate random data for the histogram
data = np.random.randn(1000) # 1000 random values from a standard normal distribution

# Create a histogram with 30 bins and black edges
plt.hist(data, bins=30, edgecolor='black')

# Add titles and axis labels
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Display the plot
plt.show()
