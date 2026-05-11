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

# Test om Läslistan startar med tom lista
@pytest.mark.unit
def test_bookstore_starts_with_empty_list():
    store = BookStore()

    assert len(store.books) == 0

# Test där book får ett unikt id
@pytest.mark.unit
def test_add_book_and_give_book_an_id():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert "id" in book

# Testar att två böcker får olika id:n.
@pytest.mark.unit
def test_add_multiple_books_gives_unique_ids():
    store = BookStore()

    book1 = store.addBook("Anna Wester", "Nybörjarkurs i Python")
    book2 = store.addBook("Anna Bergenström", "Annas mat")

    assert book1["id"] != book2["id"]

# Testar att en ny bok inte är markerad som favorit.
@pytest.mark.unit
def test_add_book_sets_favorite_to_false():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert store.hasFavorite(book["id"]) is False

# Testar att en bok kan markeras som favorit.
@pytest.mark.unit
def test_toggle_favorite_sets_book_to_true():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    store.toggleFavorite(book["id"])

    assert store.hasFavorite(book["id"]) is True

# Testar att en bok kan växla mellan favorit och inte favorit.
@pytest.mark.unit
def test_toggle_favorite_twice_sets_book_to_false():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    store.toggleFavorite(book["id"])
    store.toggleFavorite(book["id"])

    assert store.hasFavorite(book["id"]) is False

# Testar att hasFavorite på okänt id ger ValueError.
@pytest.mark.unit
def test_has_favorite_with_unknown_id_raises_error():
    store = BookStore()

    with pytest.raises(ValueError):
        store.hasFavorite(999)

# Testar att toggle_favorite på okänt id ger ValueError.
@pytest.mark.unit
def test_toggle_favorite_with_unknown_id_raises_error():
    store = BookStore()

    with pytest.raises(ValueError):
        store.toggleFavorite(999)