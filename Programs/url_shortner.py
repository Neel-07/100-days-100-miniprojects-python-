import random
import string

# Dictionary to store URL mappings (short URL to long URL)
url_mapping = {}

def generate_short_url():
    # Generate a random short URL using characters and digits
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

def shorten_url(long_url):
    # Check if the long URL is already in the dictionary
    for short_url, stored_long_url in url_mapping.items():
        if stored_long_url == long_url:
            return f"Short URL already exists: {short_url}"
    
    # Generate a new short URL and store the mapping
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return f"Short URL: http://your-short-url.com/{short_url}"

def redirect_to_long_url(short_url):
    # Redirect to the original long URL if it exists
    if short_url in url_mapping:
        return f"Redirecting to: {url_mapping[short_url]}"
    else:
        return "Short URL not found."

# Example usage
long_url = "http://www.example.com/very-long-url"
shortened_url = shorten_url(long_url)
print(shortened_url)
print(redirect_to_long_url(shortened_url.split('/')[-1]))
