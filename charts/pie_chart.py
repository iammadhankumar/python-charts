import matplotlib.pyplot as plt

# A pie chart in Python is used to represent data in a circular format, where each segment of the circle corresponds to a proportionate share of the total. 
# It's commonly used to visualize the distribution or percentage breakdown of a dataset with a limited number of categories.

# Define the labels and sizes for the pie chart
labels = ['Category A', 'Category B', 'Category C']

# Corresponding sizes for each segment
sizes = [30, 45, 25]

# Customize pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add a title to the pie chart
plt.title('Pie Chart')

# Display the plot
plt.show()