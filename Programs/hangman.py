import random

# List of words for the Hangman game (you can add more words)
word_list = ["apple", "banana", "chocolate", "elephant", "guitar", "javascript", "python", "watermelon"]

def select_random_word():
    # Select a random word from the word list
    return random.choice(word_list)

def play_hangman():
    # Initialize the game
    word_to_guess = select_random_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed
    
    # Display initial information to the player
    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    
    while attempts > 0:
        display_word = ""
        
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"Word to guess: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        if display_word == word_to_guess:
            print("Congratulations! You've guessed the word.")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print(f"Wrong guess. You have {attempts} attempts remaining.")
        else:
            print("Please enter a valid single letter guess.")
    
    if attempts == 0:
        print(f"Out of attempts. The word was '{word_to_guess}'.")

# Start the Hangman game
play_hangman()
