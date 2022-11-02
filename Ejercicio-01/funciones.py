import csv 
from Book import *

#funciona
def create_book_list(file):
    book_list = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book_list.append(BookTest(row))
        print(book_list[3])
        
        
#funciona
def list_books(file):
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['title'])


#no funciona como deberia
#def search_by(file):
    #parameter = input('Metodo de busqueda ')
    #data = input('Dato del libro ')

 #   book_list = create_book_list(file)
  #  if book_list is not None:
   #     for i in book_list:
    #        print(i)



    """
    parameter = input('Que te gustaria buscar ')
    data = input('Dato del libro ')
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row == parameter:
                print(data)
    """

#testing
x = create_book_list('Trabajo_Final_Unidad_01/libros.csv')
#y = list_books('Trabajo_Final_Unidad_01/libros.csv')
#z = search_by('Trabajo_Final_Unidad_01/libros.csv')
