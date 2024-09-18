import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f7d5ec678df5cf63398634fe8e93371'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4833'

def test_status_code():
    response_get_trainers = requests.get(url = f'{URL}/trainers')
    assert response_get_trainers.status_code == 200


def test_trainers_contains_me():
    response_trainers_contains_me = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainers_contains_me.json()['data'][0]["id"] == TRAINER_ID
  
 