class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def remove(self, book):
        self.books.remove(book)