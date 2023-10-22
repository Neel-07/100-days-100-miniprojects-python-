import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Function to calculate hand value
def calculate_hand_value(hand):
    value = 0
    aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'Ace':
            value += 11
            aces += 1
        elif rank in ['King', 'Queen', 'Jack']:
            value += 10
        else:
            # Map the string rank to its numerical value
            if rank.isdigit():
                value += int(rank)
            else:
                # Handle non-numeric ranks like 'Nine'
                if rank == 'Nine':
                    value += 9

    while aces > 0 and value > 21:
        value -= 10
        aces -= 1

    return value



# Shuffle the deck
random.shuffle(deck)

# Deal initial hands
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop()]

# Game loop
while True:
    # Calculate hand values
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # Display the cards
    print("Your hand:", [card['rank'] + ' of ' + card['suit'] for card in player_hand])
    print("Dealer's hand:", [dealer_hand[0]['rank'] + ' of ' + dealer_hand[0]['suit'], 'Unknown'])

    # Check for player blackjack
    if player_value == 21 and len(player_hand) == 2:
        print("Blackjack! You win.")
        break
    elif player_value > 21:
        print("Bust! Dealer wins.")
        break

    # Player's turn
    action = input("Do you want to 'hit' or 'stand'? ").lower()
    if action == 'hit':
        player_hand.append(deck.pop())
    elif action == 'stand':
        break

    # Dealer's turn
    if dealer_value < 17:
        dealer_hand.append(deck.pop())
    elif dealer_value >= 17:
        break

# Determine the winner
if dealer_value > 21 or player_value > dealer_value:
    print("You win!")
else:
    print("Dealer wins.")

