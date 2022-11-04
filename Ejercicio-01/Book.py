class Book:

  def __init__(self, data = {}):
    # self.id:int = None or data['id']
    self.title: str = data.get('title', None)
    self.genre: str = data.get('genre', None)
    self.isbn: str = data.get('isbn', None)
    self.editorial: str = data.get('editorial', None)
    self.authors: str = data.get('authors', None)

  def book_to_dictionary(self):
    return vars(self)

  # @staticmethod
  # def schema():
  #   return['title', 'genre', 'isbn', 'editorial', 'authors']


