import pytest
from src.bookstore import BookStore
from src.favorite_books import FavoriteBooks

# Test mellan BookStore och FavoriteBooks. Skapar bok adderar bok som favorit
# lägger den i favorit listan
@pytest.mark.integration
def test_favorite_book_can_be_added_from_bookstore():
    favorites = FavoriteBooks()
    store = BookStore(favorites)

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    store.toggleFavorite(book["id"])

    assert book in favorites.books

# Test att en favorit bok kan tas bort från favoritlistan
@pytest.mark.integration
def test_favorite_book_can_be_removed():
    favorites = FavoriteBooks()
    store = BookStore(favorites)

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    store.toggleFavorite(book["id"])
    assert book in favorites.books
    store.toggleFavorite(book["id"])
    assert book not in favorites.books

# Test att flera böcker kan adderas som favorit i Bookstore och add de kan adderas i Favoritlistan
@pytest.mark.integration
def test_multiple_favorite_books_can_be_added():
    favorites = FavoriteBooks()
    store = BookStore(favorites)

    book1 = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    book2 = store.addBook("Anna Bergenström", "Annas mat")

    store.toggleFavorite(book1["id"])
    store.toggleFavorite(book2["id"])

    assert len(favorites.books) == 2
    assert book1 in favorites.books
    assert book2 in favorites.books
