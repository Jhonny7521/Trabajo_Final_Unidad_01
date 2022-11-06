import requests
import pprint as pp

def pkm_by_gen():
    name_or_id = input("Que generacion quieres ver? ")  # name
    #name_or_id = 1         # id

    url = "https://pokeapi.co/api/v2/generation/{}/".format(name_or_id)

    response = requests.get(url)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        #pp.pprint(data)
        
        print('\n--- data.keys() ---\n')
        print(data.keys())
        
        print('\n--- Nombre de la generacion ---\n')
        print(data['name'])

        print('\n--- Pokemones en esta generacion ---\n')
        pp.pprint(data["pokemon_species"])


pkm_by_gen()