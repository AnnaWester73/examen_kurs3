class BookStore:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def addBook(self, author, title):
        book = {"id": self.next_id,"author": author,"title": title}

        self.books.append(book)
        self.next_id += 1

        return book

