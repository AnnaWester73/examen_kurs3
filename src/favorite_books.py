class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        if not self.has(book):
            self.books.append(book)

    def has(self, book):
        return book in self.books

    def toggle(self,book):
        if self.has(book):
            self.remove(book)
        else:
            self.add(book)

    def remove(self, book):
        self.books.remove(book)

    def count(self):
        return len(self.books)