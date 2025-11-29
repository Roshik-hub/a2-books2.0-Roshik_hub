"""
Test file for the Book class - CP1404 Assignment 2
Author: Roshik Maharjan
"""

from books import Book


def main():
    """Simple tests for the Book class."""
    # Test initialisation
    book = Book("Test Title", "Author Name", 300, False)
    print(book)  # Expected: "Test Title by Author Name, 300 pages"

    # Test marking completed
    print(f"Before toggle: {book.completed}")  # Expected False
    book.mark_completed()
    print(f"After toggle: {book.completed}")   # Expected True

    # Test long book detection
    long_book = Book("Long Book", "Big Author", 600, False)
    print(long_book.is_long())  # Expected True
    print(book.is_long())       # Expected False


main()
