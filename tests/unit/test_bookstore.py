import pytest
from src.bookstore import BookStore


@pytest.mark.unit
def test_add_book_returns_book_with_author_and_title():
    store = BookStore()

    book = store.addBook("Anna Wester", "Nybörjarkurs i Python")

    assert book["author"] == "Anna Wester"
    assert book["title"] == "Nybörjarkurs i Python"