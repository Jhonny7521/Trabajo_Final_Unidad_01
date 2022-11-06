class Book:

  def __init__(self, data = {}):

    self.title: str = data.get('title', None)
    self.genre: str = data.get('genre', None)
    self.isbn: str = data.get('isbn', None)
    self.editorial: str = data.get('editorial', None)
    self.authors: list = data.get('authors', None)

  def book_to_dictionary(self):
    return vars(self)




