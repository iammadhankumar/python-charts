import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Create a sample DataFrame with random data
np.random.seed(0)
df = pd.DataFrame({
    'Variable1': np.random.rand(100),  # Random values between 0 and 1
    'Variable2': np.random.rand(100) * 100,  # Random values between 0 and 100
    'Variable3': np.random.randn(100),  # Normally distributed random values
    'Category': np.random.choice(['A', 'B'], 100)  # Random categorical variable
})

# Create a pair plot with Seaborn
sns.pairplot(df, hue='Category', markers=['o', 's'])  # Color by 'Category', different markers for each category

# Add a title to the pair plot
plt.suptitle("Pair Plot Example", y=1.02)  # Adjust vertical position of the title

# Display the plot
plt.show()
