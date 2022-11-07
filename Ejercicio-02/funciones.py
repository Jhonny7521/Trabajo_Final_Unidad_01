# Funciones para las búsquedas de pokemon
import requests

# Funcion para buscar pokemon por generacion
def pkm_by_gen()-> None:
  gen = input("¿Que generacion quieres ver? Escoge del 1 al 8 o el nombre de la generacion: ")  

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

# Funcion para buscar pokemon por Habitad
def pkm_by_habit()-> None:
  name_or_id = input("¿Que habitad deseas ver? Escoge del 1 al 9 o el nombre del habitad ")  

  url = "https://pokeapi.co/api/v2/pokemon-habitat/{}/".format(name_or_id)
  response = requests.get(url)

  if response.status_code != 200: 
      print(response.text)
  else:
      data = response.json()
      
      print('\n--- Nombre del Habitad ---\n')
      print(data['name'])

      print('\n--- Pokemones en esta Habitad ---\n')

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

# Funcion para buscar pokemon por Tipo
def pkm_by_type()-> None:
  name_or_id = input("¿Que tipo de pokemon deseas ver? Escoge del 1 al 18 ó 10001 - 10002 o el nombre del habitad ")  

  url = "https://pokeapi.co/api/v2/type/{}/".format(name_or_id)
  response = requests.get(url)

  if response.status_code != 200: 
      print(response.text)
  else:
      data = response.json()
      
      print('\n--- Nombre del Tipo ---\n')
      print(data['name'])

      print('\n--- Pokemones de este Tipo ---\n')
      for pkm in data['pokemon']:
          url_pkm = pkm['pokemon']['url']
          url_number = url_pkm[len('https://pokeapi.co/api/v2/pokemon/'):-1]
          
          response2 = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(url_number))
          data2 = response2.json()
          img = data2['sprites']['front_default']

          abilities = []
          for ability in data2['abilities']:
              abilities.append(ability['ability']['name']) 

          print("El pokemon", pkm['pokemon']['name'], "tiene las habilidades", ', '.join(abilities), "y su imagen es", img)


# Funcion para buscar pokemon por Forma
def pkm_by_shape() -> None:
  name_or_id = input("¿Que forma de pokemon deseas ver? Escoge del 1 al 14 o el nombre de la forma: ")  

  url = "https://pokeapi.co/api/v2/pokemon-shape/{}/".format(name_or_id)
  response = requests.get(url)

  if response.status_code != 200: 
      print(response.text)
  else:
      data = response.json()
      
      print('\n--- Nombre de la Forma ---\n')
      print(data['name'])

      print('\n--- Pokemones en esta Forma ---\n')

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


# Funcion para buscar pokemon por Habilidad
def pkm_by_ability() -> None:
  name_or_id = input("¿Que habilidad de pokemon deseas ver? Escoge del 1 al 20 o el nombre de la forma: ")  

  url = "https://pokeapi.co/api/v2/ability/{}/".format(name_or_id)
  response = requests.get(url)

  if response.status_code != 200: 
      print(response.text)
  else:
      data = response.json()
      
      print('\n--- Nombre de la Habilidad---\n')
      print(data['name'])

      print('\n--- Pokemones con esta Habilidad ---\n')

      for pkm in data["pokemon"]:
          url_pkm = pkm['pokemon']['url']
          url_number = url_pkm[len('https://pokeapi.co/api/v2/pokemon/'):-1]

          response2 = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(url_number))
          data2 = response2.json()
          img = data2['sprites']['front_default']
          abilities = []

          for ability in data2['abilities']:
              abilities.append(ability['ability']['name'])

          print("El pokemon", pkm['pokemon']['name'], "tiene las habilidades", ', '.join(abilities), "y su imagen es", img)
