import requests
import json

api_key = "your_api_key"  # Get from OpenWeatherMap
city = input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
weather_data = response.json()

if weather_data["cod"] == 200:
    temp = weather_data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    print(f"Temperature: {temp:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found.")
