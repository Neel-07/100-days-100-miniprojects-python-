import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
pairs = [
    ["my name is (.*)", ["Hello %1! How can I assist you today?"]],
    ["(what is your name?|who are you?)", ["I am a chatbot. You can call me ChatPy."]],
    # Add more patterns and responses here
]

def chatbot():
    print("Hello! I'm your Chatbot. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main function
if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
