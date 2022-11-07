from funciones import *
from Book import *

if __name__ == "__main__":

  status = True
  print('\nBienvenid@ a tu biblioteca virtual!')
  print('Con a ayuda de este programa podras realizar las siguientes operaciones:')

  while status :

    print("\nMENÚ DE OPCIONES :\n1. Listar los 3 primeros libros\n2. Listar libros\n3. Agregar libros\n4. Eliminar libros\n5. Ordenar libros por titulo\n6. Buscar libros\n7. Actualizar libros\n8. Guardar libros en disco duro\n9. Salir del programa")
    print("---------------")
    file1 = 'books.csv'
    answer = int(input("Ingrese el numero de lo que desea hacer: "))
    print("---------------")

    if answer == 1:
      list_first_books(file1)
    elif answer ==2:
      list_books(file1)
    elif answer ==3:
      add_book(file1)
    elif answer ==4:
      delete_books(file1)
    elif answer ==5:
      sort_by_title(file1)
    elif answer ==6:
      search_by(file1)
    elif answer ==7:
      update_book(file1)
    elif answer ==8:
      save_file_to_another_path(file1)
    elif answer ==9:
      status = False
      print('Hasta luego')
    else :
      print("Por favor ingresa un número de las opciones dadas.")



