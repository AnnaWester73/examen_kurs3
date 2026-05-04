import pytest
from src.bookstore import BookStore


@pytest.mark.unit
def test_add_book_returns_book_with_author_and_title():
    store = BookStore()

    book = store.addBook("Astrid Lindgren", "Bröderna Lejonhjärta")

    assert book["author"] == "Astrid Lindgren"
    assert book["title"] == "Bröderna Lejonhjärta"