import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# A violin plot in Python is a type of plot used to visualize the distribution of a dataset, similar to a box plot, but with additional detail about the data's distribution and density. 
# It combines features of a box plot with a kernel density plot, providing a richer representation of the data.

# Generate data for the violin plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a violin plot with Seaborn
sns.violinplot(data=data)

# Add titles and axis labels
plt.title('Violin Plot')
plt.xlabel('Category')
plt.ylabel('Values')

# Display the plot
plt.show()