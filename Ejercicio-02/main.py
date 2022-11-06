# Archivo principal donde realiza la interaccion con el usuario

if __name__ == "__main__":
    from funciones import *

    print("Bienvenid@!\nEste programa te permite:\n1. Listar pokemones por generacion \n2. Listar pokemones por forma\n3. Listar pokemones por habitat\n4. Listar pokemones por tipo")
    print("---------------")
    answer = int(input("Ingrese el numero de lo que desea hacer: "))
    print("---------------")
    

    if answer ==  1:
        pkm_by_gen()
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        pass
    else:
        print('Por favor coloque una de las opciones disponibles.')
