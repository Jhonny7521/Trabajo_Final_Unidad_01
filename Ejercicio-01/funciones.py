import csv
import os

from Book import Book

# Función inicial
def init():

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
def get_data_book():

  title = input("Ingrese el título del libro: ")
  genre = input("Ingrese el género del libro: ")
  isbn = input("Ingrese el ISBN del libro: ")
  editorial = input("Ingrese el editorial del libro: ")
  autors = []

  while True:
    new_author = input('Ingrese el nombre del autor: ')
    autors.append(new_author)

    print('¿Desea agregar otro autor?: ')
    answer = check_answer()

    if not answer:
      break
  
  data_book = {
    'title': title,
    'genre': genre,
    'isbn': isbn,
    'editorial': editorial,
    'autors': autors
  }
  
  new_book = Book(data_book)

  book_data = new_book.book_to_dictionary()

  return book_data

# Función para crear un archivo csv con los nombres de cada campo
def create_file_csv(file_name):

  field_names = ['title', 'genre', 'isbn', 'editorial', 'authors']

  with open(file_name, mode='w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
     
    # writing headers (field names)
    writer.writeheader()

    csvfile.close()

# Función para agregar un registro de un nuevo libro
def save_book_data(file_name, book_data):

  field_names = ['title', 'genre', 'isbn', 'editorial', 'authors']

  with open(file_name, mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= field_names)
    writer.writerow(book_data)

    csvfile.close()


# Función para verificar las respuestas del usuario
def check_answer():
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