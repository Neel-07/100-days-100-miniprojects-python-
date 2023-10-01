import pyttsx3

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Input the text to convert to speech
text = input("Enter the text to convert to speech: ")

# Convert text to speech
text_to_speech(text)
