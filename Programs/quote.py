import random

def generate_random_quote(quotes):
    try:
        random_quote = random.choice(quotes)
        return random_quote
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create a list of quotes
quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
]

# Generate and display a random quote
random_quote = generate_random_quote(quotes)
print("Random Quote:")
print(random_quote)
