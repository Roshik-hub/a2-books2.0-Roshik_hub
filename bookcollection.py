"""
BookCollection class for Assignment 2 - CP1404

Author: Roshik Maharjan
Date: 28/11/2025
"""

import json
from books import Book

class BookCollection:
    """Manage a collection of Book objects."""

    def __init__(self):
        """Initialize an empty book list."""
        self.books = []

    def load_books(self, filename):
        """Load books from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)
        for entry in data:
            book = Book(entry["title"], entry["author"], int(entry["pages"]), entry["completed"])
            self.books.append(book)

    def save_books(self, filename):
        """Save books to a JSON file."""
        with open(filename, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, book: Book):
        """Add a book to the collection."""
        self.books.append(book)

    def get_pages_to_read(self):
        """Return total pages of unread books."""
        return sum(book.pages for book in self.books if not book.completed)

    def sort_books(self, key):
        """Sort books by the given attribute."""
        self.books.sort(key=lambda b: getattr(b, key))
