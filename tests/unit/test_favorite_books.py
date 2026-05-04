import pytest
from src.favorite_books import FavoriteBooks


@pytest.mark.unit
def test_add_book_to_favorites():
    favorites = FavoriteBooks()

    book = {"id": 1, "title": "Test", "author": "Test"}

    favorites.add(book)

    assert book in favorites.books


@pytest.mark.unit
def test_remove_book_from_favorites():
    favorites = FavoriteBooks()

    book = {"id": 1, "author": "Anna Wester", "title": "Nybörjarkurs i Python"}

    favorites.add(book)
    favorites.remove(book)

    assert book not in favorites.books