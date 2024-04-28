import networkx as nx
import matplotlib.pyplot as plt

# A network graph in Python is used to visualize the connections between different nodes, often representing relationships, dependencies, or connections in a dataset. 
# It's useful for illustrating complex networks like social relationships, transportation systems, or communication networks.
# If needed, install networkx
# pip install networkx

# Create a simple graph with nodes and edges
G = nx.Graph()  # Use nx.DiGraph() for directed graphs

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Add edges to represent connections between nodes
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('B', 'D')])

# Draw the network graph
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_color='black', edge_color='gray')

# Add a title
plt.title("Network Graph Example")

# Display the plot
plt.show()
