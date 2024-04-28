import matplotlib.pyplot as plt

# An area chart in Python is used to display the filled area between a line (representing a variable) and a baseline (typically the x-axis). 
# It can be helpful to visualize cumulative data, trends, or comparisons between multiple series.

# Data for the area chart
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 25, 30, 35]
y2 = [5, 10, 20, 25, 30]

# Create the area chart with improved style
plt.figure(figsize=(8, 6))  # Set the figure size

# Fill the area between y1 and y2 with a specific color and transparency
plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4)

# Add titles and labels
plt.title("Area Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Customize axes ticks and limits
plt.xticks(x)  # Set the x-axis ticks to match the x values
plt.yticks(range(0, 40, 5))  # Set the y-axis ticks from 0 to 35 with a step of 5

# Add a grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

# Add axis limits for better control over the plot area
plt.xlim(1, 5)  # Set x-axis limits
plt.ylim(0, 40)  # Set y-axis limits

# Display the plot
plt.show()
