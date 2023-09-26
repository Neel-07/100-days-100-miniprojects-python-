import requests

def get_weather(city):
    api_key = "a46204c99e856ef2b7517cb7bc2f4086"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        return f"Weather in {city}: {description}, Temperature: {temperature}°C, Humidity: {humidity}%"
    else:
        return "Weather information not available."

# Input a city name
city = input("Enter a city name: ")

# Get and print the weather information
weather_info = get_weather(city)
print(weather_info)
