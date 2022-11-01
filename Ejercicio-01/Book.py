class Book:

  def __init__(self, data):
    self.id:int = None or data['id']
    self.title: str = None or data['title'] 
    self.genre: str = None or data['genre']
    self.ISBN: str = None or data['ISBN']
    self.editorial: str = None or data['editorial']
    self.authors: str = None or data['authors']


