"""
Test file for the BookCollection class - CP1404 Assignment 2
Author: Roshik Maharjan
"""

from bookcollection import BookCollection
from books import Book


def main():
    """Simple tests for the BookCollection class."""
    collection = BookCollection()

    # Test adding books
    collection.add_book(Book("Book A", "Author A", 300, False))
    collection.add_book(Book("Book B", "Author B", 200, True))
    print(f"Books loaded: {len(collection.books)}")  # Expected 2

    # Test pages to read
    print(collection.get_pages_to_read())  # Expected 300

    # Test sorting
    collection.sort_books("title")
    print(collection.books[0].title)  # Expected "Book A"

    collection.sort_books("pages")
    print(collection.books[0].pages)  # Expected 200

    # Test JSON save/load (manual check required)
    collection.save_books("test_books.json")
    print("Saved to test_books.json")


main()
