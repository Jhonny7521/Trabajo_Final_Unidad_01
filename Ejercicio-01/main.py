from funciones import *
from Book import *

if __name__ == "__main__":

  status = True
  print('\nBienvenid@ a tu biblioteca virtual!')
  print('Con a ayuda de este programa podras realizar las siguientes operaciones:')

  while status :

    print("\nMENÚ DE OPCIONES :\n1. Listar libros\n2. Agregar libros\n3. Eliminar libros\n4. Buscar libros\n5. Actualizar libros\n6. Guardar libros en disco duro\n7. Salir del programa")
    print("---------------")
    file1 = 'books.csv'
    answer = int(input("Ingrese el numero de lo que desea hacer: "))
    print("---------------")

    if answer == 1:
      list_books(file1)
    elif answer ==2:
      add_book(file1)
    elif answer ==3:
      delete_books(file1)
    elif answer ==4:
      search_by(file1)
    elif answer ==5:
      update_book(file1)
    elif answer ==6:
      save_file_to_another_path(file1)
    elif answer ==7:
      status = False
      print('Hasta luego')
    else :
      print("Por favor ingresa un número de las opciones dadas.")



