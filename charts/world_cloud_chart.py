from wordcloud import WordCloud
import matplotlib.pyplot as plt

# A word cloud in Python is used to visually represent the frequency of words in a text. The more frequently a word appears in the text, the larger it appears in the word cloud.
# This type of visualization is useful for text analysis, helping to quickly identify commonly used words and patterns.
# If needed, install the wordcloud library
# pip install wordcloud

# Define the text for the word cloud
text = """
    Python is an amazing language. It is great for data analysis, data visualization,
    machine learning, and many other applications. Python's simplicity and readability 
    make it an excellent choice for beginners and professionals alike.
"""

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')  # Use bilinear interpolation for better rendering
plt.axis('off')  # Hide axes
plt.title("Word Cloud Example")
plt.show()
