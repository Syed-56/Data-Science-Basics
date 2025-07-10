import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)


    if response.status_code == 200: #for successful connection
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Error: {response.status_code}")

pokemonName = "pikachu"
pokemon = get_pokemon(pokemonName)

if pokemon:
    print(pokemon['name'])