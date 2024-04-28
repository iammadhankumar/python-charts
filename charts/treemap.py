import matplotlib.pyplot as plt
import squarify

# Sample data for the treemap
data = {
    'Category A': 100,
    'Category B': 75,
    'Category C': 50,
    'Category D': 25,
    'Category E': 10
}

# Create a treemap
plt.figure(figsize=(8, 8))
squarify.plot(sizes=list(data.values()), 
              label=list(data.keys()), 
              alpha=0.8, 
              color=['skyblue', 'orange', 'green', 'red', 'purple'])

# Add a title
plt.title("Treemap Example")

# Hide the axes for better visualization
plt.axis('off')

# Display the plot
plt.show()
