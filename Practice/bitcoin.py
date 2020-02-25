import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
bitcoin_data = requests.get(url).json()
conversionFactor = bitcoin_data['bpi']['USD']['rate_float']
print(conversionFactor)
print()
numBit = float(input('How many bit coin do you have? '))
dollhairs = numBit*conversionFactor
print(f'You have, {dollhairs} dollhairs.')