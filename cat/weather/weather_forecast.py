import os

import requests
from pprint import pprint
import re

# SET UP PROGRAM
def main():
    city, state, countryCode = getInput()
    valid_city, valid_state, valid_countryCode = validate(city, state, countryCode)
    data = getData(valid_city, valid_state, valid_countryCode)
    fiveDay = storeData(data)
    displayData(fiveDay)

# GET DATA FROM USER
def getInput():
    city = input('\nWhat is the name of the city you want a forecast for? ')
    state = input('What is the name of the state or province? Enter n/a if there is none. ')
    countryCode = input('What is your countries two letter code? ')

    return city, state, countryCode

# VAIDATE DATA
def validate(city, state, countryCode):
    while True:
        if state.upper()=='N/A':
            state = ''
        else:
            state+=' ,'
        while len(countryCode)<2 or len(countryCode)>2 or not countryCode.isalpha():
            countryCode = input('Please enter valid country code, two letters no more no less. ')

        data =  getData(city, state, countryCode)

        if data['cod'] != '404':
            break
        
        city = input('\nThere appears to have been an error finding the city you want the forecast for.\nPlease consider the spelling.\nWhat is the name of the city you would like the weather for? ')
        state = input('Please enter the two letter code for the state or province, enter N/A if there is none. ')
        countryCode = input('please enter a valid two digit country code. ')

    return city, state, countryCode

# GET DATA
def getData(city, state, countryCode):
    key = os.environ.get('WEATHER_KEY')
    query = {'q':str(city)+','+str(state)+str(countryCode), 'units': 'imperial', 'appid':key}

    url = 'https://api.openweathermap.org/data/2.5/forecast'

    data = requests.get(url, params=query).json()

    return data    

# STORE DATA
def storeData(data):
    fiveDay = {}
    
    
    for hour in range(len(data['list'])):
        if hour%8==0:
            weatherTimes=[]
            da = data['list'][hour]['dt_txt']
            # Solutions for regex
            # https://www.tutorialspoint.com/How-to-extract-date-from-text-using-Python-regular-expression
            # https://stackoverflow.com/questions/18493677/how-do-i-return-a-string-from-a-regex-match-in-python
            day = re.search(r'\d{4}-\d{2}-\d{2}', da).group(0)
            fiveDay.update({ day : weatherTimes})
        wData=[]
        # TODO I chose to local time because that is what I personally prefer to 
        # look at as a user, also because I'm feeling ill and I just want to get 
        # this done.
        tim = data['list'][hour]['dt_txt']
        time = re.search(r'\d{2}:\d{2}:\d{2}',tim).group(0)
        temp = data['list'][hour]['main']['temp']
        desc = data['list'][hour]['weather'][0]['description']
        wind = data['list'][hour]['wind']['speed']
        wData.append([time, temp, desc, wind])
        weatherTimes.append(wData)
        fiveDay.update({day : weatherTimes})

    return fiveDay

# DISPLAY DATA
def displayData(fiveDay):
    print('\nThis is the 5 day weather forecast\n')
    # Solution for iterating through dictionary
    # https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
    for date, wList in fiveDay.items():
        print('Date: '+str(date)+'\n')
        for value in wList:
            print('\tTime: '+str(value[0][0]))
            print('\tTemp: '+str(value[0][1])+'F')
            print('\tConditions: '+str(value[0][2]))
            print('\tWindspeed: '+str(value[0][3])+'mph\n')

if __name__ == '__main__':
    main()