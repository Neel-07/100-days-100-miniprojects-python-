from gtts import gTTS

def convert_text_to_audio(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Example usage:
text_content = "This is a sample text to be converted into an audio book."
convert_text_to_audio(text_content, 'sample_audio_book.mp3')
