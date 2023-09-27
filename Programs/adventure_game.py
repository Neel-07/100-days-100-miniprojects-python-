import time

def game_over():
    print("Game over. Try again!")
    time.sleep(2)
    # You can add more options to restart or exit the game here

def start_game():
    print("Welcome to the Text-based Adventure Game!")
    print("You find yourself in a mysterious forest.")
    
    choice = input("Do you want to go 'left' or 'right'? ").lower()
    
    if choice == 'left':
        print("You find a hidden treasure!")
        time.sleep(2)
        print("Congratulations, you win!")
    elif choice == 'right':
        print("You encounter a dragon!")
        time.sleep(2)
        print("The dragon breathes fire and...")
        time.sleep(2)
        game_over()
    else:
        print("Invalid choice. Try again.")
        start_game()

# Start the game
start_game()
