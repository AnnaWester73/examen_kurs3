class BookStore:
    def __init__(self):
        self.books = []

    def addBook(self, author, title):
        book = {"author": author,"title": title}

        self.books.append(book)
        return book

