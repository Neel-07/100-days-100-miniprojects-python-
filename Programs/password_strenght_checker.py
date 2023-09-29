import re

def check_password_strength(password):
    # Define password strength criteria
    length_criteria = len(password) >= 8
    complexity_criteria = re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*]', password)
    
    if length_criteria and complexity_criteria:
        return "Strong password!"
    elif length_criteria:
        return "Moderate password. Consider adding numbers and special characters."
    else:
        return "Weak password. Password should be at least 8 characters long."

# Input a password to check
password = input("Enter a password: ")

# Check password strength
strength_result = check_password_strength(password)
print(strength_result)

