import matplotlib.pyplot as plt
import numpy as np

# A stacked line chart in Python is used to show the cumulative effect of multiple data series stacked on top of each other. It's a variation of a line chart where the lines represent 
# the cumulative total at each point, demonstrating how multiple datasets contribute to a total over time.

# Generate data for the stacked line chart
x = np.arange(10)  # X-axis values, representing time or some other progression
y1 = np.random.randint(1, 10, 10)  # First data series
y2 = np.random.randint(1, 10, 10)  # Second data series
y3 = np.random.randint(1, 10, 10)  # Third data series

# Calculate cumulative values for stacked lines
y_stack = np.vstack([y1, y2, y3]).cumsum(axis=0)  # Cumulative sum along the rows

# Create a stacked line chart
plt.figure(figsize=(10, 6))
plt.fill_between(x, y_stack[0], color='skyblue', label='Series 1')  # Fill between x-axis and first data series
plt.fill_between(x, y_stack[1], y_stack[0], color='orange', label='Series 2')  # Between first and second
plt.fill_between(x, y_stack[2], y_stack[1], color='green', label='Series 3')  # Between second and third

# Add titles and labels
plt.title("Stacked Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Cumulative Value")

# Add a legend
plt.legend()

# Display the plot
plt.show()
