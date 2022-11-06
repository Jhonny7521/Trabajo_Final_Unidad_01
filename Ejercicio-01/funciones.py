import csv
import os

from Book import Book

# Función inicial
def init() -> None:

  start_excersice = True

  while start_excersice:
    print('¿Desea agregar un nuevo libro?')
    answer = check_answer()

    if answer :
      book_data = get_data_book()

      file_name = 'books.csv'
      content = os.path.isfile(file_name)

      if not content:
        create_file_csv(file_name)
        save_book_data(file_name, book_data)
      else:
        save_book_data(file_name, book_data)

    else:
      start_excersice = False


# Función que retorna un objeto libro en forma de diccionario luego de obtener los datos
def get_data_book() -> dict:

  # Instanciamos una clase Book
  new_book = Book()

  new_book.title = input("Ingrese el título del libro: ")
  new_book.genre = input("Ingrese el género del libro: ")
  new_book.isbn = input("Ingrese el ISBN del libro: ")
  new_book.editorial = input("Ingrese el editorial del libro: ")
  autors = []

  # Consultamos si el libro contiene más de 1 autor
  while True:
    new_author = input('Ingrese el nombre del autor: ')
    autors.append(new_author)

    print('¿Desea agregar otro autor?: ')
    answer = check_answer()

    if not answer:
      break

  new_book.authors = autors

  # Obtenemos los datos de la clase en forma de diccionario
  book_data = new_book.book_to_dictionary()

  return book_data

# Función para crear un archivo csv con los nombres de cada campo
def create_file_csv(file_name: str) -> None:

  # nombres de los campos de cada libro
  field_names = ['title', 'genre', 'isbn', 'editorial', 'authors']

  with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
    # Creamos el objeto de escritura para el archivo cvs
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
     
    # Escribimos los nombres de los campos
    writer.writeheader()
    # Cerramos el archivo cvs
    csvfile.close()

# Función para agregar un registro de un nuevo libro
def save_book_data(file_name: str, book_data : dict) -> None:

  # nombres de los campos de cada libro
  field_names = ['title', 'genre', 'isbn', 'editorial', 'authors']

  with open(file_name, mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= field_names)

    # Agregamos una fila mas al archivo cvs con los datos nuevos
    writer.writerow(book_data)

    # Cerramos el archivo cvs
    csvfile.close()


# Función para verificar las respuestas del usuario
def check_answer() -> bool:

  is_correct = True

  while True:

    answer = input('Ingrese su respuesta Y / N: \n').upper()

    if answer.upper() == "N":
      is_correct = False
      break
    elif answer.upper() == "Y":
      is_correct = True
      break
    else:
      print('Ingrese una respuesta valida\n')
    
  return is_correct