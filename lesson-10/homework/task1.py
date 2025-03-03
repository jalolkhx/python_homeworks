import requests
import json
from city_info import capital_cities

city = input("Enter a capital city: ").lower()
try:
    lat = capital_cities[city.capitalize()]["lat"]  # find the error
    lon = capital_cities[city.capitalize()]["lon"]
except Exception as e:
    raise IndexError("Invalid capital city!")

api_key = "8f9324e53a2c2702566a21c3436aeb0a"

url = "https://api.openweathermap.org/data/3.0/onecall"
params = {
    "appid": api_key,
    "lat": lat,
    "lon": lon
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print("Daily weather info: ")
    print(f"Summary: {data['daily'][0]['weather'][0]['description']}")
    print(f"Temperature (day): {round(float(data['daily'][0]['temp']['day'])-273.15, 1)} °C")
    print(f"Temperature (night): {round(float(data['daily'][0]['temp']['night'])-273.15, 1)} °C")
    print(f"Humidity: {data['daily'][0]['humidity']} %")
    print(f"Wind speed: {data['daily'][0]['wind_speed']} m/s")
