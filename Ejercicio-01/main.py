from funciones import *
from Book import *

if __name__ == "__main__":

    init()

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
            delete_books(file1)
        case 4:
            search_by(file1)
        case 5:
            update_book(file1)
        case 6:
            pass
        case default:
            print("Por favor ingresa un numero de las opciones dadas.")


