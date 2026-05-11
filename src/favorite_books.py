class FavoriteBooks:
    def __init__(self):
        self.books = []

    # Lägger till en bok om den inte redan finns i favoriter.
    def add(self, book):
        if not self.has(book):
            self.books.append(book)

    # Kontrollerar om en bok är markerad som favorit.
    def has(self, book):
        return book in self.books

    # Växlar favoritstatus: lägger till om boken saknas, tar bort om den finns.
    def toggle(self, book):
        if self.has(book):
            self.remove(book)
        else:
            self.add(book)

    # Tar bort en bok från favoriter.
    def remove(self, book):
        self.books.remove(book)

    # Returnerar antalet favoritböcker.
    def count(self):
        return len(self.books)