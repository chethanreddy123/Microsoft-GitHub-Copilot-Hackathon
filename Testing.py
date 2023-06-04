import requests
import json
import sys

def get_weather(city):
    api_key = "17039d6beb4b43a0294f19509cc88fd7"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather forecast for {city}:")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)

    city_name = " ".join(sys.argv[1:])
    get_weather(city_name)
