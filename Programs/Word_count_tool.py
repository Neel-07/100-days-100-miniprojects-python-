def count_words(text):
    words = text.split()
    return len(words)

# Input a text paragraph
paragraph = input("Enter a paragraph: ")

# Get and print the word count
word_count = count_words(paragraph)
print(f"Word count: {word_count}")
