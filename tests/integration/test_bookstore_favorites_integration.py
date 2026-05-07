import pytest
from src.bookstore import BookStore
from src.favorite_books import FavoriteBooks

# Test mellan BookStore coh FavoriteBooks. Skapar bok adderar bok som favorit
# lägger den i favorit listan
@pytest.mark.integration
def test_favorite_book_can_be_added_from_bookstore():
    store = BookStore()
    favorites = FavoriteBooks()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    favorite_book = store.toggleFavorite(book["id"])
    favorites.add(favorite_book)

    assert favorite_book in favorites.books

# Test att en favorit bok kan tas bort från favoritlistan
@pytest.mark.integration
def test_favorite_book_can_be_removed():
    store = BookStore()
    favorites = FavoriteBooks()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    favorite_book = store.toggleFavorite(book["id"])
    favorites.add(favorite_book)

    favorites.remove(favorite_book)

    assert favorite_book not in favorites.books

# Test att flera böcker kan adderas som favorit i Bookstore och add de kan adderas i Favoritlistan
@pytest.mark.integration
def test_multiple_favorite_books_can_be_added():
    store = BookStore()
    favorites = FavoriteBooks()

    book1 = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    book2 = store.addBook("Anna Bergenström", "Annas mat")

    favorite_book1 = store.toggleFavorite(book1["id"])
    favorite_book2 = store.toggleFavorite(book2["id"])

    favorites.add(favorite_book1)
    favorites.add(favorite_book2)

    assert len(favorites.books) == 2
    assert favorite_book1 in favorites.books
    assert favorite_book2 in favorites.books


# Testar att en favoritmarkerad bok refererar till samma objekt i både
# BookStore och FavoriteBooks
@pytest.mark.integration
def test_favorite_book_is_same_object_as_in_bookstore():
    store = BookStore()
    favorites = FavoriteBooks()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    favorite_book = store.toggleFavorite(book["id"])
    favorites.add(favorite_book)

    # Boken i butiken och i favoriter ska vara samma objekt i minnet.
    assert favorites.books[0] is store.books[0]
    assert favorites.books[0]["favorite"] is True