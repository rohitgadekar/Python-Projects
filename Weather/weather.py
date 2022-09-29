from urllib import response
import requests
import os
import cred

API_KEY = cred.api_key  # API KEY FROM OPEN WEATHER
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # BASE URL

print("Dragon Weather Finder")
for i in range(1, 22):
    print("-", end="")
city = input("\nEnter City Name :: ")  # INPUTS

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"  # REQUEST URL

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    country = data["sys"]["country"]
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]['pressure']
    os.system("cls")
    print("City            :: ", city, country)
    print("Weather         :: ", weather)
    print("Temperature     :: ", round(int(temperature) - 273.15), "°C")
    print("Humidity        :: ", humidity, '%')
    print("Pressure        :: ", pressure, "hPa")
else:
    print("Error Occured")
