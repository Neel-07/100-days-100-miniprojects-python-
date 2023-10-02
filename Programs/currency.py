import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        # You can use a currency exchange rate API (e.g., exchangerate-api.com)
        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(api_url)
        data = response.json()
        
        if to_currency in data['rates']:
            conversion_rate = data['rates'][to_currency]
            converted_amount = amount * conversion_rate
            return f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}"
        else:
            return "Invalid target currency."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Input the amount, source currency, and target currency
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the source currency code (e.g., USD): ").upper()
to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

# Perform the currency conversion
conversion_result = convert_currency(amount, from_currency, to_currency)
print(conversion_result)
