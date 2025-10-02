import os
import requests
from pprint import pprint

# Minneapolis Latitude and Longitude
lat = 44.97
lon = -93.26
units = 'metric'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc. 

api_key = os.environ['WEATHER_KEY']  # Set this environment variable on your computer 

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

response = requests.get(url)
weather_forecast = response.json()
# pprint(weather_forecast)

# Extract and print some information from the JSON response
# Getting different pieces of information from the JSON response
weather_description = weather_forecast['list'][0]['weather'][0]['description']
wind_key = weather_forecast['list'][0]['wind']
wind_gusts = weather_forecast['list'][0]['wind']['gust']
# print(f'Current weather: {weather_description}')
# print(f'Current wind: {wind_key}')
# print(f'Current wind gusts: {wind_gusts}')

for interval in weather_forecast['list']:
    dt_txt = interval['dt_txt']
    temp = interval['main']['temp']
    description = interval['weather'][0]['description']
    print(f'At {dt_txt}, the temperature will be {temp}°C with {description}.')