import random

def create_flashcards():
    flashcards = {}
    
    while True:
        native_word = input("Enter a word or phrase in your native language (or type 'exit' to finish): ")
        
        if native_word.lower() == 'exit':
            break
        
        translation = input(f"Enter the translation of '{native_word}' in the target language: ")
        
        flashcards[native_word] = translation
    
    return flashcards

def test_flashcards(flashcards):
    keys = list(flashcards.keys())
    random.shuffle(keys)
    
    correct_count = 0
    
    for key in keys:
        user_translation = input(f"What is the translation of '{key}' in the target language? ")
        
        if user_translation == flashcards[key]:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong. The correct translation is '{flashcards[key]}'")
    
    print(f"You got {correct_count} out of {len(keys)} correct.")

# Create flashcards
flashcards = create_flashcards()

# Test the user's knowledge
test_flashcards(flashcards)
