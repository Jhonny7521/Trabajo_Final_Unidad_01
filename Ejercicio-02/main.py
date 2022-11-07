# Archivo principal donde realiza la interaccion con el usuario
from funciones import *

if __name__ == "__main__":

  status = True
  print('\nBienvenid@ a tu Pokedex virtual!')
  print('Con a ayuda de este programa podras realizar las siguientes operaciones:')

  while status:
      
    print("MENÚ DE OPCIONES:\n1. Listar pokemones por generacion \n2. Listar pokemones por forma\n3. Listar pokemones por habilidad\n4. Listar pokemones por habitad\n5. Listar pokemones por tipo\n6. Salir del programa")
    print("---------------")
    answer = int(input("Ingrese el numero de lo que desea hacer: "))
    print("---------------")
    

    if answer ==  1:
      pkm_by_gen()
    elif answer == 2:
      pkm_by_shape()
    elif answer == 3:
      pkm_by_ability()
    elif answer == 4:
      pkm_by_habit()
    elif answer == 5:
      pkm_by_type()
    elif answer == 6:
      status = False
      print('Hasta luego')
    else:
      print('Por favor coloque una de las opciones disponibles.')
