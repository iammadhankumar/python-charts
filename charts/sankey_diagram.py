import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Create a Sankey diagram
sankey = Sankey(flows=[8, -4, -3, -1],  # Positive for inputs, negative for outputs
                labels=['Input', 'Output 1', 'Output 2', 'Loss'],
                orientations=[0, 1, 1, -1])  # Directions for the flows

plt.figure(figsize=(10, 6))
sankey.finish()

# Add a title
plt.title("Sankey Diagram Example")

# Display the plot
plt.show()
