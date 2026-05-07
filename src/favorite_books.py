class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove(self, book):
        self.books.remove(book)

    def count(self):
        return len(self.books)