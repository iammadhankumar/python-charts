import matplotlib.pyplot as plt
import numpy as np

# A waterfall chart in Python is used to visualize the cumulative effect of sequentially added or subtracted values, 
# often employed in financial or business analysis to show the flow of values or changes over time. 
# It helps to understand the breakdown of gains and losses, or increases and decreases, within a series of data.
# If needed, install `waterfall_chart` library
#pip install waterfall_chart

# Define the categories and values for the waterfall chart
categories = ['Start', 'Increase', 'Decrease', 'Another Increase', 'End']
values = [100, 50, -30, 20, 140]  # Changes to apply at each step

# Calculate the cumulative sums to plot
cumulative = np.cumsum(values)  # Cumulative total at each step
start_values = np.insert(cumulative[:-1], 0, 0)  # Start points for each step

# Create a figure
plt.figure(figsize=(10, 6))

# Plot the waterfall chart
for i in range(len(categories)):
    if values[i] >= 0:
        plt.bar(categories[i], values[i], bottom=start_values[i], color='green')
    else:
        plt.bar(categories[i], values[i], bottom=start_values[i], color='red')

# Add connecting lines to show the flow
for i in range(1, len(categories)):
    plt.plot([categories[i - 1], categories[i]], [cumulative[i - 1], start_values[i]], 'k-', linewidth=1)

# Add titles and labels
plt.title("Waterfall Chart Example")
plt.xlabel("Steps")
plt.ylabel("Values")

# Display the plot
plt.show()
