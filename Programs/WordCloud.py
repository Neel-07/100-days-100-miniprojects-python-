from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    # Generate a word cloud from the given text
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    # Display the word cloud using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Main function
if __name__ == "__main__":
    text = input("Enter the text for the word cloud: ")
    
    generate_word_cloud(text)
