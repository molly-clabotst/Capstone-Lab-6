from weather_api_key import key

import os

import requests
from pprint import pprint 

def main():
    keyy = os.environ.get('WEATHER_KEY')
    query = {'q':'minneapolis,mn,us', 'units': 'imperial', 'appid':keyy}

    url = 'https://api.openweathermap.org/data/2.5/weather'

    data = requests.get(url, params=query).json()
    # pprint(data)
    weather_description = data['weather'][0]['description']
    temp_f = data['main']['temp']
    temp_feels = data['main']['feels_like']

    # pprint(data)
    print(f'Today in Minneapolis there are {weather_description} out.\n\nThe temperature is {temp_f:.2f}F but it feels like {temp_feels:.2f}F.\n')

if __name__ == '__main__':
    main()
