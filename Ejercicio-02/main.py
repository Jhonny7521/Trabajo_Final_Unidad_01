if __name__ == "__main__":
    from pokeapi_funciones import *

    print("Bienvenid@!\nEste programa te permite:\n1. Listar pokemones por generacion \n2. Listar pokemones por forma\n3. Listar pokemones por habitat\n4. Listar pokemones por tipo")
    print("---------------")
    answer = int(input("Ingrese el numero de lo que desea hacer: "))
    print("---------------")
    
    match answer:
        case 1:
            pkm_by_gen()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case default:
            print("Por favor ingresa un numero de las opciones dadas.")