import requests

url = 'https://catfact.ninja/fact'
cat_data = requests.get(url).json()
fact = cat_data['fact']
print(fact)
print()
print(cat_data)