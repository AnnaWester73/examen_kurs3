from .favorite_books import FavoriteBooks

class BookStore:
    def __init__(self, favorite_books=None):
        self.books = []
        self.next_id = 1
        self.favorite_books = favorite_books or FavoriteBooks()

    # Skapar en ny bok med författare och titel, sparar den och returnerar boken.
    def addBook(self, author, title):
        book = {"id": self.next_id, "author": author, "title": title}

        self.books.append(book)
        self.next_id += 1

        return book

    # Kontrollerar om boken med angivet id är markerad som favorit.
    # Kastar ValueError om ingen bok med id:t finns.
    def hasFavorite(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return self.favorite_books.has(book)

        raise ValueError(f"Ingen bok med id {book_id}")

    # Växlar favoritstatus för boken med angivet id.
    # Delegerar till FavoriteBooks.toggle().
    # Kastar ValueError om ingen bok med id:t finns.
    def toggleFavorite(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                self.favorite_books.toggle(book)
                return

        raise ValueError(f"Ingen bok med id {book_id}")