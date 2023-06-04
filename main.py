from API import owm  # Importing the owm module from the API
from pyowm.commons.exceptions import NotFoundError  # Importing the NotFoundError exception from the pyowm module
from datetime import datetime  # Importing the datetime module


def weather_detail(place, unit):
    # Initializing the weather manager
    mgr = owm.weather_manager()

    days = []  # List to store unique dates
    dates_2 = []  # List to store all dates
    min_t = []  # List to store minimum temperatures
    max_t = []  # List to store maximum temperatures

    # Getting the forecast and current weather for the specified place
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    obs = mgr.weather_at_place(place)
    weather = obs.weather

    # Getting the temperature in Celsius or Fahrenheit based on the unit provided
    temperature = weather.temperature(unit='celsius')['temp']
    if unit == 'Celsius':
        unit_c = 'celsius'
    else:
        unit_c = 'fahrenheit'

    # Looping through the forecast to extract temperature data for each day
    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date1 = day.date()

        # Storing unique dates in the days list
        if date1 not in dates_2:
            dates_2.append(date1)
            min_t.append(None)
            max_t.append(None)
            days.append(date1)

        temperature = weather.temperature(unit_c)['temp']

        # Updating the minimum and maximum temperatures for each day
        if not min_t[-1] or temperature < min_t[-1]:
            min_t[-1] = temperature
        if not max_t[-1] or temperature > max_t[-1]:
            max_t[-1] = temperature

    # Getting the current weather information
    obs = mgr.weather_at_place(place)
    weather = obs.weather

    # Printing the current weather details
    print(f"📍 Weather at {place[0].upper() + place[1:]} currently: ")
    if unit_c == 'celsius':
        print(f"## 🌡️ Temperature: {temperature} °C")
    else:
        print(f"## 🌡️  Temperature: {temperature} F")
    print(f"### ☁️ Sky: {weather.detailed_status}")
    print(f"### 🌪  Wind Speed: {round(weather.wind(unit='km_hour')['speed'])} km/h")
    print(f"### ⛅️Sunrise Time :     {weather.sunrise_time(timeformat='iso')} GMT")
    print(f"### ☁️  Sunset Time :      {weather.sunset_time(timeformat='iso')} GMT")

    # Expected Temperature Alerts
    print("❄️Expected Temperature Changes/Alerts: ")
    if forecaster.will_have_fog():
        print("### ▶️FOG ALERT🌁!!")
    if forecaster.will_have_rain():
        print("### ▶️RAIN ALERT☔!!")
    if forecaster.will_have_storm():
        print("### ▶️STORM ALERT⛈️!!")
    if forecaster.will_have_snow():
        print("### ▶️ SNOW ALERT❄️!!")
    if forecaster.will_have_tornado():
        print("### ▶️TORNADO ALERT🌪️!!")
    if forecaster.will_have_hurricane():
        print("### ▶️HURRICANE ALERT🌀")
    if forecaster.will_have_clear():
        print("### ▶️CLEAR WEATHER PREDICTED🌞!!")
    if forecaster.will_have_clouds():
        print("### ▶️CLOUDY SKIES⛅")

    print()
    print()

    # Printing the maximum and minimum temperatures for each date
    i = 0
    print("# 📆 Date :  Max - Min  ({unit})")
    for obj in days:
        ta = (obj.strftime("%d/%m"))
        print(f'### ➡️ {ta} :\t   ({max_t[i]} - {min_t[i]})')
        i += 1


# Taking user input for city name and temperature unit
place = input("Enter the city name: ")
unit = input('Celsius", "Fahrenheit" : ')

if place != "":
    try:
        weather_detail(place, unit)
    except NotFoundError:
        print("Please enter a Valid city name")
