class BookTest:
  def __init__(self, data):
    self.title = data.get('title', None)
    self.author = data.get('author', None)
    self.genres = data.get('genres', None)
    self.publisher = data.get('publisher', None)
    self.isbn = data.get('isbn', None)

  def __str__(self):
    return f'El libro {self.title}, fue escrito por {self.author}.\nEs del genero {self.genres} y fue publicado por {self.publisher}'

