import matplotlib.pyplot as plt

# A line chart in Python is used to represent data points connected by lines, often to visualize trends, changes over time, or relationships between variables. 
# The given code snippet creates a simple line chart with Matplotlib, providing basic plot elements like titles and axis labels.

# Define x and y values for the line chart
x = [1, 2, 3, 4, 5]  # X-axis values
y = [10, 12, 5, 8, 3]  # Y-axis values

# Create line plot
plt.plot(x, y)

# Add titles and axis labels
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()