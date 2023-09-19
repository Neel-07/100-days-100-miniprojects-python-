import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_letters if use_uppercase else string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) < 1:
        return "Invalid configuration."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User-defined options
password_length = 16
include_uppercase = True
include_numbers = True
include_special_chars = True

# Generate the random password
generated_password = generate_password(
    password_length, include_uppercase, include_numbers, include_special_chars
)

print(f"Generated Password: {generated_password}")
