
class Book:
  def __init__(self, data):
    self.title = data.get('title', None)
    self.authors = data.get('author', None)
    self.genres = data.get('genres', None)
    self.editorial = data.get('publisher', None)
    self.isbn = data.get('isbn', None)

  def __str__(self):
    return f'El libro {self.title}, fue escrito por {self.authors}.\nEs del genero {self.genres} y fue publicado por {self.editorial}'
"""

class Book:
    def init (self):
        self.title: str = None
        self.genre: str = None
        self.isbn: str = None
        self.publisher: str = None
        self.authors: str = None

    def set_title(self, title_book: str):
        self.title = title_book

    def set_genre(self, genre_book: str):
        self.genre = genre_book

    def set_isbn(self, isbn_book: str):
        self.isbn = isbn_book

    def set_publisher(self, publisher_book: str):
        self.publisher = publisher_book

    def set_authors (self, authors_book: str):
        self.authors = authors_book

    def book_to_dictionary (self):
        return vars(self)

    #def __str__(self):
     #   return f'El libro {self.title}, fue escrito por {self.author}.\nEs del genero {self.genres} y fue publicado por {self.publisher}'
"""