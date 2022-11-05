if __name__ == "__main__":

    from funciones_jj import *
    from Book import *

    print("Bienvenid@!\nEste programa te permite:\n1. Listar libros\n2. Agregar libros\n3. Eliminar libros\n4. Buscar libros\n5. Actualizar libros\n6. Guardar libros")
    print("---------------")
    file1 = input("Ingrese el path del archivo que desea utilizar: ")
    answer = int(input("Ingrese el numero de lo que desea hacer: "))
    print("---------------")


    match answer:
        case 1:
            list_books(file1)
        case 2:
            pass
        case 3:
            pass
        case 4:
            search_by(file1)
        case 5:
            pass
        case 6:
            pass
        case default:
            print("Por favor ingresa un numero de las opciones dadas.")

