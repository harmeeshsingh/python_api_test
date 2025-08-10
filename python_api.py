#information using python
import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Not able to reterive the data\nError: {response.status_code}" )

pokemon_name = input("Enter the name of your favorite pokemon: ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Order: {pokemon_info['order']}")

