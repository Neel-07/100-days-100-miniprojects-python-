import demoji

# Initialize the demoji library
demoji.download_codes()

# Sample text with emojis
text_with_emojis = "I love coding! 😎🚀👩‍💻"

# Decode emojis within the text
decoded_text = demoji.replace_with_desc(text_with_emojis)

# Print the original text and decoded text
print("Original Text: " + text_with_emojis)
print("Decoded Text: " + decoded_text)
