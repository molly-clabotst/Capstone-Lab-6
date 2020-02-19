import requests
from weather_api_key import key
from pprint import pprint 

def main():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,us&units=imperial&appid=' + key()
    data = requests.get(url).json()
    weather_description = data['weather'][0]['description']
    temp_f = data['main']['temp']
    temp_feels = data['main']['feels_like']

    # pprint(data)
    print(f'Today in Minneapolis there are {weather_description} out.\n\nThe temperature is {temp_f} but it feels like {temp_feels}.\n')

if __name__ == '__main__':
    main()
