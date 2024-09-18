import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f7d5ec678df5cf63398634fe8e93371'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = body_create_pokemon)


body_put_pokemon = {
    "pokemon_id": "72004",
    "name": "NewName",
    "photo_id": 997
}
response1 = requests.put(url = f'{URL}/pokemons', headers = HEADER , json = body_put_pokemon)


body_add_pokeball = {
    "pokemon_id": "72004"
}
response2 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_add_pokeball)


print(response.text)
print(response1.text)
print(response2.text)