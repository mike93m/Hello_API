import os
import requests
import logging
from pprint import pprint
from datetime import datetime

# Set up logging configuration.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():

    # Retrieve the API key from environment variables. The key should be saved on your system as an environment variable.
    api_key = os.environ['WEATHER_KEY']  

    # Minneapolis Latitude and Longitude.
    # Used for the API call to get the weather forecast.
    lat = 44.97
    lon = -93.26
    units = 'imperial'  # Temperature units, change to 'metric' for quantities in Celsius
    
    # Set temperature unit symbol based on units. Used in the output table header.
    if units == 'imperial':
        temp_unit = '°F'
    else:
        temp_unit = '°C'    

    # Construct the API URL with the latitude, longitude, units, and API key.
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

    try: # Try block to catch potential request exceptions

        # Make the API request and store the JSON response.
        response = requests.get(url)
        weather_forecast = response.json()

    except requests.exceptions.RequestException as e:
        print(f'Error fetching weather data: {e}')
        return

    # These variables are for testing purposes to ensure I am getting the expected values.
    weather_description = weather_forecast['list'][0]['weather'][0]['description']
    wind_key = weather_forecast['list'][0]['wind']
    wind_gusts = weather_forecast['list'][0]['wind']['gust']

    # Log tessting
    logging.debug(f'Current weather: {weather_description}\n')
    logging.debug(f'Current wind: {wind_key}\n')
    logging.debug(f'Current wind gusts: {wind_gusts}\n')

    print("Here is the 5 day weather forecast for Minneapolis, MN:\n")
    print("The weather forecast is provided in 3 hour intervals.\n")

    # Print a header for the forecast table
    print(f"{'Time':<10} {'Day':<10} {'Date':<15} {f'Temp {temp_unit}':<12} {'Description':<25} {'Wind (m/s)':<12} {'Gusts (m/s)':<12}")
    print("-" * 101)

    
    try: # Try block to catch potential KeyErrors or ValueErrors

        # Loop through the list of weather data and print the forecast
        for interval in weather_forecast['list']:  # Each interval is a 3 hour forecast

            # Extract the time and date and convert from Unix timestamp to readable format.
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

    except (KeyError, ValueError, TypeError) as e:
        print(f'Error processing weather data: {e}')
        return

if __name__ == '__main__':
    main()