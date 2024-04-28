import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# A box plot in Python is used to visualize the distribution of data, highlighting the median, quartiles, and potential outliers within a dataset. 
# It's a useful visualization tool for understanding the spread, skewness, and potential anomalies in the data.

# Create data for the box plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create the box plot with additional customization
sns.boxplot(data=data)

# Add a title and axis labels 
plt.title('Box Plot')
plt.xlabel('Category')
plt.ylabel('Values')

# Display the plot
plt.show()  # Show the plot