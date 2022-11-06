import csv 
from Book import *

#funciona
def create_book_list(file):
    book_list = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book_list.append(Book(row))
        return book_list
        
        
#funciona
def list_books(file):
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['title'])


#funciona
def search_by(file):
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
            if data in book.genres:
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


#testing
#x = create_book_list('Trabajo_Final_Unidad_01/Ejercicio-01/libros.csv')
#y = list_books('Trabajo_Final_Unidad_01/Ejercicio-01/libros.csv')
z = search_by('Trabajo_Final_Unidad_01/Ejercicio-01/libros.csv')
#a = author_number('Trabajo_Final_Unidad_01/Ejercicio-01/libros.csv')