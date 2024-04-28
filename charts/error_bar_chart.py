import matplotlib.pyplot as plt
import numpy as np

# An error bar chart in Python is a type of chart used to show the uncertainty or variability in data points. 
# It's common in scientific experiments and studies where data has inherent measurement errors or statistical variations. 
# Error bars can represent standard deviation, standard error, confidence intervals, or other measures of variability.

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]  # Mean values for each category
errors = [2, 3, 4, 1]  # Corresponding error values (e.g., standard deviation)

# Create a bar chart with error bars
plt.figure(figsize=(8, 6))
plt.bar(categories, values, yerr=errors, capsize=5, color='skyblue', alpha=0.7, ecolor='red')

# Add titles and labels
plt.title("Bar Chart with Error Bars")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the plot
plt.show()
