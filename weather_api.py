import requests

API_KEY = "your_openweathermap_api_key"

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"Current temperature in {location} is {temp}°C with {desc}."
    else:
        return "Sorry, I couldn't get weather information for that location."

# Example use:
print(get_weather("Chennai"))
