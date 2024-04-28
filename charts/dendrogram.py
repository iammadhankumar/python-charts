import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# A dendrogram in Python is a tree-like diagram used to illustrate the arrangement of clusters produced by hierarchical clustering algorithms. 
# It's commonly used in data analysis and bioinformatics to visualize the relationships and groupings within a dataset.

# Generate sample data for clustering
np.random.seed(0)
data = np.random.rand(10, 2)  # 10 points with 2 features

# Perform hierarchical clustering
linked = linkage(data, 'single')  # 'single' linkage, other options include 'complete', 'average', etc.

# Create a dendrogram
plt.figure(figsize=(10, 6))
dendrogram(linked, 
           orientation='top',  # Orientation of the dendrogram ('top', 'right', 'bottom', 'left')
           labels=[f'Point {i}' for i in range(10)],  # Custom labels for the leaves
           distance_sort='descending',  # Sort distances
           show_leaf_counts=True)  # Display the count of each leaf in the dendrogram

# Add titles and labels
plt.title("Dendrogram Example")
plt.xlabel("Cluster Distance")
plt.ylabel("Points")

# Display the plot
plt.show()
