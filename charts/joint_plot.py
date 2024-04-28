import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# A joint plot in Python is used to visualize the relationship between two variables along with their marginal distributions. It combines a scatter plot (or other types of plots) with histograms or density
# plots on the margins to provide additional context on the individual variable distributions.
# If needed, install Seaborn
# pip install seaborn

# Create a sample DataFrame with random data
np.random.seed(0)
df = pd.DataFrame({
    'Variable1': np.random.rand(100),  # Random values between 0 and 1
    'Variable2': np.random.rand(100) * 100,  # Random values between 0 and 100
})

# Create a joint plot with Seaborn (scatter plot with marginal histograms)
joint_plot = sns.jointplot(x='Variable1', y='Variable2', data=df, kind='scatter', color='blue')

# Add a title to the joint plot
joint_plot.fig.suptitle("Joint Plot Example", y=1.05)  # Adjust title position to avoid overlapping with the plot

# Display the plot
plt.show()
