import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
