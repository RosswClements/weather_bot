import requests
from pyfiglet import figlet_format
import datetime
import config

ascii_art = figlet_format("WeatherBot")
print(ascii_art)


api_key = config.api_key

city_name = input("Enter a location: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(url)

data = response.json()

today = datetime.date.today()
todays_date = today.strftime("%d %B, %Y")
name = data['name']
country = data['sys']['country']
description = data['weather'][0]['description'].capitalize()
temp = round(int(data['main']['temp']) - 273.15)
humid = data['main']['humidity']
feel = round(int(data['main']['feels_like']) - 273.15)
maxi = round(int(data['main']['temp_max']) - 273.15)
mini = round(int(data['main']['temp_min']) - 273.15)
sunrise = datetime.datetime.fromtimestamp(int(data['sys']['sunrise'])).strftime('%H:%M')
sunset = datetime.datetime.fromtimestamp(int(data['sys']['sunset'])).strftime('%H:%M')


#print(data)
print(f"{name} {country}, {todays_date}:")
print(f"{description} & {temp}°C")
print(f"Feels like {feel}°C")
print(f"Max temperature: {maxi}°C")
print(f"Min temperature: {mini}°C")
print(f"Humidity: {humid}%")
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")


