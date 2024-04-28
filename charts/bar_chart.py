import matplotlib.pyplot as plt

# A bar chart in Python is used to visualize categorical data, where each bar represents a category and its height or length represents a value associated with that category. 
# Bar charts are useful for comparing different categories, visualizing distributions, or showing trends over time.

# Original data
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 20]

# Original bar chart code
plt.bar(categories, values)
plt.title('Bar Chart')  # Original title
plt.xlabel('Categories')  # Original x-axis label
plt.ylabel('Values')  # Original y-axis label

# Display the plot
plt.show()