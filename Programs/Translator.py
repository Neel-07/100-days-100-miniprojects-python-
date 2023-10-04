from googletrans import Translator

def translate_text(text, source_language, target_language):
    try:
        # Initialize the translator
        translator = Translator()

        # Perform the translation
        translated_text = translator.translate(text, src=source_language, dest=target_language)
        
        return translated_text.text

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Input text, source language, and target language
text_to_translate = input("Enter the text to translate: ")
source_language = input("Enter the source language code (e.g., 'en' for English): ")
target_language = input("Enter the target language code (e.g., 'es' for Spanish): ")

# Translate and display the text
translated_text = translate_text(text_to_translate, source_language, target_language)
print("Translated Text:")
print(translated_text)
