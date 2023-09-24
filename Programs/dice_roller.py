import random

def roll_dice():
    return random.randint(1, 6)

while True:
    user_input = input("Roll the dice? (yes/no): ").lower()
    
    if user_input == 'yes':
        result = roll_dice()
        print(f"You rolled a {result}")
    elif user_input == 'no':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
