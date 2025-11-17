

import requests
import json

def get_pokemon(name_or_id):   #  function that takes argument and returns a dictionary

 url = 'https://pokeapi.co/api/v2/pokemon/'  # url for api request


response = requests.get(url) # api request

if response.status_code != 200:
    raise ValueError('Pokemon not found')  # if pokemon doesnt exist show error

   data = json.loads(response.text)  # convert JSON text into Python dict

return {
        "name": pokemon_data['name'],
        "weight_kg": weight,
        "height_m": height,
        "ability": ability
    }



































































