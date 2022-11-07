# Funciones para las búsquedas de pokemon

import requests
import pprint as pp

#buscar pokemon por generacion
def pkm_by_gen():
    name_or_id = input("Que generacion quieres ver? ")  

    url = "https://pokeapi.co/api/v2/generation/{}/".format(name_or_id)

    response = requests.get(url)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        
        print('\n--- data.keys() ---\n')
        print(data.keys())
        
        print('\n--- Nombre de la generacion ---\n')
        print(data['name'])

        print('\n--- Pokemones en esta generacion ---\n')
        pp.pprint(data["pokemon_species"])


def pkm_by_form() -> None:

  status = True

  print('Que forma de pokemon quieres ver?\n Puede ingresar valores como 1, 2, 3, etc o también el nombre directo del pokemon como bulbasaur, charmander, squirtle, etc \n')

  while status:

    name_or_id = input('Ingrese su respuesta: ')  

    url = f"https://pokeapi.co/api/v2/pokemon-form/{name_or_id}/"

    response = requests.get(url)

    if response.status_code != 200: 

      print(response.text)
      print('El valor o pokemon ingresado no es correcto')

    else:

      status = False
      data = response.json()
      
      pokemon_name = data['pokemon']['name']
      pokemon_image = data['sprites']['front_default']

      pokemon_url = data['pokemon']['url']

      resp = requests.get(pokemon_url)

      if resp.status_code != 200: 
        print(resp.text)

      else:
        new_data = resp.json()

        pokemon_ability = []

        abilities = new_data['abilities']

        for ability in abilities:
          pokemon_ability.append(ability['ability']['name'])
      
      print('\n--- Nombre de pokemon ---\n')
      print(pokemon_name)
      
      print('\n--- Habilidades ---\n')

      for ability in pokemon_ability:
        print(ability)
      
      print('\n--- Url de imagen ---\n')
      print(pokemon_image)


