import csv
import os
import shutil

from Book import Book

# Función inicial
def add_book(file_name) -> None:

  start_excersice = True

  while start_excersice:
    print('¿Desea agregar un nuevo libro?')
    answer = check_answer()

    if answer :
      book_data = get_data_book()

      # file_name = 'books.csv'
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

#crear lista de libros
def create_book_list(file) -> list: 
    book_list = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book_list.append(Book(row))
        return book_list
        
        
#hacer lista de libros
def list_books(file) -> list: 
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['title'])


#funcion de busqueda
def search_by(file) -> str:
    parameter = input('Metodo de busqueda:\nPuedes usar las opciones: titulo, autor, editorial, genero, isbn.\nIngresa tu metodo de busqueda: ')

    book_list = create_book_list(file)

    #busqueda por titulo
    if parameter == 'titulo':
        data = input('Dato del libro ')
        title_search = next(
            (book for book in book_list if book.title == data),
            None
        )
        print(title_search)


    #busqueda por autor y numero de autores
    elif parameter == 'autor':
        author_num = input('Cuantos autores tiene tu libro? ')
        if author_num == '1':
            data = input('Dato del libro ')
            author_search = next(
                (book for book in book_list if book.authors == data),
                None
            )
            print(author_search) 
        else: 
            author_int = int(author_num) - 1
            for book in book_list: 
                results = book.author.count(',')
                if author_int == results: 
                    print(f"El libro {book.title}, fue escrito por {book.authors}")

    #busqueda por editorial
    elif parameter == 'editorial':
        data = input('Dato del libro ')
        publisher_search = next(
            (book for book in book_list if book.editorial == data),
            None
        )
        print(publisher_search) 

    #busqueda por genero
    elif parameter == 'genero':
        data = input('Dato del libro ')
        for book in book_list:
            if data in book.genre:
                print(book.title)

    #busqueda por isbn
    elif parameter == 'isbn':
        data = input('Dato del libro ')
        isbn_search = next(
            (book for book in book_list if book.isbn == data),
            None
        )
        print(isbn_search)    

    #mensaje de error, reinicia el loop
    else: 
        print('Una de las opciones es incorrecta\nPor favor coloque una de las opciones\n----------------------')
        search_by(file)

# Funcion de actulizacion o modificacion de datos de un libro
def update_book(file):
    file_update = open(file,'r')
    Reader = csv.reader(file_update)
    L = []
    uId = input('Ingresa el nombre del Libro que deseas actualizar o modificar: ').lower()
    found = False
    for row in Reader:
        if row[0].lower() == uId:
            found = True
            print(row[0],' - ',row[1],' - ',row[2],' - ',row[3],' - ',row[4])
            title_new = input('Ingrese un nuevo Titulo: ')
            genre_new = input('Ingrese un nuevo Genero: ')
            isbn_new = input('Ingrese un nuevo ISBN: ')
            publisher_new = input('Ingrese una nueva Editorial: ')
            author_new = input('Ingrese un nuevo Autor(es), separado por coma: ')
            row[0] = title_new
            row[1] = genre_new
            row[2] = isbn_new
            row[3] = publisher_new
            row[4] = author_new
        L.append(row)
    file_update.close()

    if found == False:
        print('Libro no encontrado.')
    else:
        file_update = open(file,'w+',newline='')
        Writer = csv.writer(file_update)
        Writer.writerows(L)
        file_update.seek(0)
        Reader = csv.reader(file_update)
        for row in Reader:
            print(row)
        file_update.close()

# Funcion de eliminacion de libros segun su nombre
def delete_books(file):
    lines = list()
    book_name = input('Ingresa el nombre del Libro a ser eliminado: ').lower()
    with open(file,'r') as File:
        reader = csv.reader(File)
        for row in reader:
            lines.append(row)
            for field in row:
                if field.lower() == book_name:
                    lines.remove(row)
    
    with open(file,'w+',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

# Funcion para guardar el archivo generado en otra direccion que ingrese el usuario
def save_file_to_another_path(file_name:str) -> None:

  status = True

  while status:
    new_path = input('Ingrese la direccion donde desea guardar su archivo: \n')

    print('El nombre del archivo por defecto es "book.csv".\n¿Desea guardar el archivo con otro nombre?\n')

    answer = check_answer()

    try:
      if answer:
        new_file_name = input('Ingrese el nuevo nombre para el archivo: ')
        shutil.copy(file_name, f'{new_path}/{new_file_name}.csv')
      else:
        shutil.copy(file_name, f'{new_path}/{file_name}')
      
      status = False
      print('Archivo guardado correctamente')

    except:
      print('Ha ocurrido un error con la ruta ingresada. Por favor ingrese una ruta valida.')
