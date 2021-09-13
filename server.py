import json
import requests
from requests import HTTPError, ConnectionError

def http_error(error):
    return {
        "Error": True,
        "Message": f"We have a http_error(error: {error}), try again."
    }

def connection_error(error):
    return {
        "Error": True,
        "Message": f"We have a connection_error(error: {error}), try again."
    }

def default_error():
    return {
        "Error": True,
        "Message": "This pokémon don't exist or don't was found. Try again."
    }

def get_pokemon(pokemon_name: str):
    if pokemon_name == '':
        return default_error()
    
    pokemon = pokemon_name.lower()

    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        api = requests.get(url)
        response = json.loads(api.text)
        abilities = []

        for ability in response['abilities']:
            ability_name = ability['ability']['name']
            abilities.append(ability_name)
        
        name = response['name']
        types = []

        for type in response['types']:
            type_name = type['type']['name']
            types.append(type_name)
        
        pokedex_id = response['id']
        height = response['height']
        weight = response['weight']
        specie = response['species']['name']
        moves = []

        for move in response['moves']:
            move_name = move['move']['name']
            moves.append(move_name)
        
        img = response['sprites']['front_default']
        pokemon_data = {
            "name": name,
            "height": height,
            "weight": weight,
            "id": pokedex_id,
            "specie": specie,
            "moves": moves,
            "types": types,
            "abilities": abilities,
            "img": img
        }

        return pokemon_data

    except HTTPError as e:
        return http_error(e)
    except ConnectionError as e:
        return connection_error(e)
    except IndexError:
        return default_error()
    except:
        return default_error()

if __name__ == '__main__':
    print(get_pokemon('ditto'))