import json

# Function to add a new password
def add_password(account, username, password):
    # Create or load a JSON file to store passwords
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Store the password securely (you can implement encryption here)
    data[account] = {'username': username, 'password': password}

    # Save the updated data
    with open('passwords.json', 'w') as file:
        json.dump(data, file)

# Function to retrieve a password
def get_password(account):
    # Load the stored passwords
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            if account in data:
                return data[account]
            else:
                return "Account not found."
    except FileNotFoundError:
        return "No passwords stored yet."

# Example usage
add_password('example.com', 'user123', 'securepass123')
print(get_password('example.com'))
