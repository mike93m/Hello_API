import requests
import os

def main():

    key = os.environ.get('WEATHER_KEY')
    if key is None:
        print('Error: No API key found.')
        return
    
    city_country = input('Enter a city and country code (e.g., minneapolis,us): ')
    city_country = city_country.strip().lower()
    city = city_country.split(',')[0].title()
    


    query = {'q': city_country, 'units': 'imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/weather'

    data = requests.get(url, params=query).json()
    weather_description = data['weather'][0]['description']

    temp_f = data['main']['temp']
    print(f'The current weather in {city} is: {weather_description}, the temperature is {temp_f:.2f}°F')

if __name__ == '__main__':
    main()