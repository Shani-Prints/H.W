from app.library import Library
from app.book import Book
import pytest

@pytest.fixture
def library():
    lib = Library()
    lib.add_user("Shani")
    return lib

@pytest.fixture
def book():
    return Book("aaa", "Avigail")

def test_add_book(library):
    book = Book("aaa", "Shani")
    library.add_book(book)
    assert book in library.books

def test_add_user(library):
    library.add_user("Shani")
    assert "Shani" in library.users


def test_add_user_empty_name(library):
    with pytest.raises(ValueError, match="Username must not be empty."):
        library.add_user("")

def test_check_out_book_success(library, book):
    library.add_book(book)
    library.check_out_book("Shani", book)
    assert book.is_checked_out is True
    assert library.checked_out_books["Shani"] == book


def test_check_out_nonexistent_book(library, book):
    with pytest.raises(ValueError, match=f"Book '{book.title}' by {book.author} is not in the library."):
        library.check_out_book("Shani", book)

def test_return_book_success(library, book):
    library.add_book(book)
    library.check_out_book("Shani", book)
    assert book.is_checked_out is True
    assert library.checked_out_books["Shani"] == book
    library.return_book("Shani", book)
    assert book.is_checked_out is False
    assert "Shani" not in library.checked_out_books


def test_search_books_exact_match(library):
    book1 = Book("aaa", "bbb")
    book2 = Book("ccc", "ddd")
    library.add_book(book1)
    library.add_book(book2)
    result = library.search_books("aaa")
    assert len(result) == 1
    assert result[0] == book1


def test_check_out_nonexistent_book(library):
    book = Book("Book", "Unknown Author")
    with pytest.raises(ValueError, match=f"Book '{book.title}' by {book.author} is not in the library."):
        library.check_out_book("Shani", book)

def test_check_out_to_unregistered_user(library, book):
    library.add_book(book)
    with pytest.raises(ValueError, match="User 'UnregisteredUser' is not registered."):
        library.check_out_book("UnregisteredUser", book)


def test_add_user_empty_name(library):
    with pytest.raises(ValueError, match="Username must not be empty."):
        library.add_user("")
