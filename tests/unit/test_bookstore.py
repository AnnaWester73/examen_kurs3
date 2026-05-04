import pytest
from src.bookstore import BookStore

# Test att skapa en book med författare och title
@pytest.mark.unit
def test_add_book_returns_book_with_author_and_title():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert book["author"] == "Anna Wester"
    assert book["title"] == "Nybörjarkurs i Python"

# Test att spara en bok i listan
@pytest.mark.unit
def test_add_book_stores_book_in_list():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert book in store.books

# Test att spara flera böcker i listan
@pytest.mark.unit
def test_add_multiple_books_in_book_stores():
    store = BookStore()

    store.addBook("Anna Wester", "Nybörjarkurs i Python")
    store.addBook("Anna Bergenström", "Annas mat")

    assert len(store.books) == 2

# Test om boklistan är tom
@pytest.mark.unit
def test_bookstore_starts_with_empty_list():
    store = BookStore()

    assert store.books == []

# Test där book får ett unikt id
@pytest.mark.unit
def test_add_book_and_give_book_an_id():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert "id" in book

# Testar som kollar om en bok INTE är markerad som favorit
@pytest.mark.unit
def test_add_book_sets_favorite_to_false():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert book["favorite"] is False


# Test som kollar om en bok är markerad som favorit
@pytest.mark.unit
def test_toggle_favorite_sets_book_to_true():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    store.toggleFavorite(book["id"])

    assert book["favorite"] is True


# Test att man kan ändra bok fram och tillbaka som favorit.
@pytest.mark.unit
def test_toggle_favorite_twice_sets_book_to_false():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    store.toggleFavorite(book["id"])
    store.toggleFavorite(book["id"])

    assert book["favorite"] is False
