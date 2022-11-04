class Book:

  def __init__(self):
    # self.id:int = None or data['id']
    self.title: str = None
    self.genre: str = None
    self.isbn: str = None
    self.editorial: str = None
    self.authors: str = None

  def set_title(self, title_book: str):
    self.title = title_book

  def set_genre(self, genre_book: str):
    self.genre = genre_book

  def set_isbn(self, isbn_book: str):
    self.isbn = isbn_book

  def set_editorial(self, editorial_book: str):
    self.editorial = editorial_book

  def set_authors(self, authors_book: str):
    self.authors = authors_book

  def book_to_dictionary(self):
    return vars(self)

  # @staticmethod
  # def schema():
  #   return['title', 'genre', 'isbn', 'editorial', 'authors']


