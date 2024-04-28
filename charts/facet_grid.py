import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample DataFrame
np.random.seed(0)
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], 100),  # Randomly assign categories
    'Value1': np.random.randn(100),  # 100 random values
    'Value2': np.random.rand(100) * 100  # 100 random values between 0 and 100
})

# Create a facet grid with scatter plots
g = sns.FacetGrid(df, col='Category', col_wrap=2)  # Facet by 'Category' with 2 columns per row
g.map_dataframe(sns.scatterplot, x='Value1', y='Value2')  # Map scatter plots to the grid

# Add titles and adjust layout
g.fig.suptitle("Facet Grid Example with Scatter Plots", y=1.05)  # Add a super title to the grid
g.set_axis_labels("Value1", "Value2")  # Set axis labels

# Display the plot
plt.show()
