import matplotlib.pyplot as plt
import numpy as np

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
