import pytest
from src.favorite_books import FavoriteBooks


# Testar att en bok kan läggas till i favoriter.
@pytest.mark.unit
def test_add_book_to_favorites():
    favorites = FavoriteBooks()

    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.add(book)

    assert book in favorites.books

# Testar att en bok kan tas bort från favoriter.
@pytest.mark.unit
def test_remove_book_from_favorites():
    favorites = FavoriteBooks()

    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.add(book)
    favorites.remove(book)

    assert book not in favorites.books

# Testar att en ny favoritlista är tom.
@pytest.mark.unit
def test_favorites_starts_empty():
    favorites = FavoriteBooks()

    assert favorites.books == []


# Testar att count returnerar rätt antal favoriter.
@pytest.mark.unit
def test_count_returns_number_of_favorites():
    favorites = FavoriteBooks()
    favorites.add({"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"})
    favorites.add({"id": 2, "author": "Anna Bergenström", "title": "Annas mat"})

    assert favorites.count() == 2


# Testar att samma bok inte läggs till två gånger.
@pytest.mark.unit
def test_add_same_book_twice_only_stores_once():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.add(book)
    favorites.add(book)

    assert favorites.count() == 1

# Testar att has() returnerar True för en bok som är i favoriter.
@pytest.mark.unit
def test_has_returns_true_when_book_in_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.add(book)

    assert favorites.has(book) is True

# Testar att has() returnerar False för en bok som inte är i favoriter.
@pytest.mark.unit
def test_has_returns_false_when_book_not_in_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    assert favorites.has(book) is False

# Testar att toggle() lägger till en bok som inte är favorit.
@pytest.mark.unit
def test_toggle_adds_book_when_not_in_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.toggle(book)

    assert favorites.has(book) is True

# Testar att toggle() tar bort en bok som redan är favorit.
@pytest.mark.unit
def test_toggle_removes_book_when_in_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.add(book)
    favorites.toggle(book)

    assert favorites.has(book) is False
