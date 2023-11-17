import requests

# Function to check the status of a URL
def check_url_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"{url} is live."
        else:
            return f"{url} is not live. Status code: {response.status_code}"
    except requests.ConnectionError:
        return f"{url} is unreachable."

# Example list of URLs to check
urls_to_check = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.nonexistenturl123.com"
]

# Checking status for each URL
for url in urls_to_check:
    print(check_url_status(url))
