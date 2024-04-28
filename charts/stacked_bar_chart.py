import matplotlib.pyplot as plt
import numpy as np

# A stacked bar chart in Python is used to show the relative composition of different categories within a total. 
# Each bar represents a group, and the different segments within each bar represent subcategories. 
# Stacked bar charts are helpful for comparing categories and their subcomponents. 
# You can create stacked bar charts with libraries like Matplotlib, Seaborn, or Plotly.

# Data for the bar chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
subcategories = ['Subcat 1', 'Subcat 2', 'Subcat 3']

# Data for each subcategory within each category
data = np.array([
    [10, 15, 20],  # Category A
    [20, 25, 30],  # Category B
    [30, 35, 40],  # Category C
    [40, 45, 50]   # Category D
])

# Define the base position for each bar
bar_width = 0.5
positions = np.arange(len(categories))

# Create the stacked bar chart
plt.figure(figsize=(10, 6))

# Plot the first subcategory
bottom = np.zeros(len(categories))  # Start from zero for the first subcategory
for i, subcat in enumerate(subcategories):
    plt.bar(positions, data[:, i], bar_width, label=subcat, bottom=bottom, color=plt.cm.viridis(i / len(subcategories)))
    bottom += data[:, i]  # Update the bottom to stack the next subcategory

# Add titles and labels
plt.title("Stacked Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Add a legend to identify the subcategories
plt.legend(title="Subcategories")

# Display the plot
plt.xticks(positions, categories)  # Set x-axis ticks to category names
plt.show()
