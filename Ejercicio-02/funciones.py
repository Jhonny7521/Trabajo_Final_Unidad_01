# Funciones para las búsquedas de pokemon

import requests
import pprint as pp

#buscar pokemon por generacion
def pkm_by_gen():
    gen = input("Que generacion quieres ver? ")  

    url = "https://pokeapi.co/api/v2/generation/{}/".format(gen)
    

    response = requests.get(url)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        
        print('\n--- Nombre de la generacion ---\n')
        print(data['name'])

        print('\n--- Pokemones en esta generacion ---\n')

        for pkm in data["pokemon_species"]:
            url_pkm = pkm['url']
            url_number = url_pkm[len('https://pokeapi.co/api/v2/pokemon-species/'):-1]


            response2 = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(url_number))

            data2 = response2.json()

            img = data2['sprites']['front_default']

            abilities = []

            for ability in data2['abilities']:
                abilities.append(ability['ability']['name'])


            print("El pokemon", pkm['name'], "tiene las habilidades", ', '.join(abilities), "y su imagen es", img)
            
        #pp.pprint(data["pokemon_species"])




pkm_by_gen()