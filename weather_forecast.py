import os
import requests
import logging
from pprint import pprint
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Minneapolis Latitude and Longitude
# Used for the API call to get the weather forecast
lat = 44.97
lon = -93.26
units = 'imperial'  # Tempurature units, change to 'metric' for quantities in Fahrenheit

api_key = os.environ['WEATHER_KEY']  # Set this environment variable on your computer 

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

# Make the API request and store the JSON response
response = requests.get(url)
weather_forecast = response.json()

# Ensure a valid response was received
logging.debug(f'Weather forecast data: {pprint(weather_forecast)}')

# Extract and print some information from the JSON response
weather_description = weather_forecast['list'][0]['weather'][0]['description']
wind_key = weather_forecast['list'][0]['wind']
wind_gusts = weather_forecast['list'][0]['wind']['gust']

# Testing to make sure I am getting the correct expected values
logging.debug(f'Current weather: {weather_description}')
logging.debug(f'Current wind: {wind_key}')
logging.debug(f'Current wind gusts: {wind_gusts}')

print("Here is the 5 day weather forecast for Minneapolis, MN:")
print("The weather forecast is provided in 3 hour intervals.\n")

# Print a header for the forecast table
print(f"{'Time':<10} {'Day':<10} {'Date':<15} {'Temp (°F)':<12} {'Description':<25} {'Wind (m/s)':<12} {'Gusts (m/s)':<12}")
print("-" * 101)

# Loop through the list of weather data and print the forecast
for interval in weather_forecast['list']:  # Each interval is a 3 hour forecast

    # Extract the time and date and convert from Unix timestamp to readable format
    time_stamp = interval['dt'] 
    time = datetime.fromtimestamp(time_stamp) 
    formatted_time = time.strftime("%I:%M %p") # Format time as HH:MM AM/PM
    date = datetime.fromtimestamp(time_stamp).date() 
    formatted_date = date.strftime("%b %d, %Y") # Format date as Month Day, Year
    day_of_week = date.strftime("%A") # Get the day of the week

    # Extract the temperature, wind speed, wind gusts, and weather description
    temp = interval['main']['temp']
    wind_speed = interval['wind']['speed']
    wind_gusts = interval['wind']['gust']
    description = interval['weather'][0]['description']

    print(f'{formatted_time:<10} {day_of_week:<10} {formatted_date:<15} {temp:<12.1f} {description:<25} {wind_speed:<12.1f} {wind_gusts:<12.1f}')
    print()
