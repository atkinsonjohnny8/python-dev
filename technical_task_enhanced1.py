
import json
import requests
from random import randint
while True:
    try:
        choice = int (input('Enter your choice number:'))  
        break
    except ValueError:
        print("This is not a number")    
   
url=f'https://api.punkapi.com/v2/beers/?id={choice}'
r= requests.get(url)
data= json.loads(r.text)

beer_list = []

for beer in data:
    name = beer['name']
    
    beer_item = {
        'name': name
      
    }
    beer_list.append(beer_item)

value = randint(0, len(beer_list))
toma = beer_list[value]
try_name = toma['name']


print(f'You should try {try_name}')