import random

def fortune_teller():
    # List of fortunes or advice
    fortunes = [
        "You will have a day filled with joy and laughter.",
        "A big opportunity is just around the corner. Seize it!",
        "Take some time for self-care today. You deserve it.",
        "Your hard work will pay off soon. Keep going!",
        "An old friend will reach out to you. Reconnect with them.",
        "Today is a day for new beginnings. Embrace change."
    ]

    # Randomly select a fortune
    random_fortune = random.choice(fortunes)
    
    return random_fortune

# Get a random fortune
random_fortune = fortune_teller()
print("Fortune Teller says:")
print(random_fortune)
