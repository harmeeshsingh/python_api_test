import requests

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Pokemon '{name}' \nError: {response.status_code}")
        return None

if __name__ == "__main__":
    print("Welcome to the Pokémon Info Program!")
    print("Type the name of a Pokémon to get its details.")
    print("Type 'end' anytime to quit.\n")
    
    query_count = 0 
    while True:
        
        query_count += 1
        print(f"Your query number is: {query_count}")

        pokemon_name = input("Enter Pokémon name: ").lower().strip()

        if pokemon_name == "end":
            print("Thanks for using the Pokémon Info Program! Goodbye 👋")
            break

        pokemon_info = get_pokemon_info(pokemon_name)

        if pokemon_info:
            print(f"\nName: {pokemon_info['name']}")
            print(f"Height: {pokemon_info['height']}")
            print(f"Weight: {pokemon_info['weight']}")
            types = [t['type']['name'] for t in pokemon_info['types']]
            print(f"Types: {', '.join(types)}\n")
