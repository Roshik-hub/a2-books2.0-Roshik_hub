"""
Book class for Assignment 2 - CP1404

Author: Roshik Maharjan
Date: 27/11/2025
"""

class Book:
    """Represent a Book object."""

    def __init__(self, title="", author="", pages=0, completed=False):
        """Initialize a book with title, author, pages, and completion status."""
        self.title = title
        self.author = author
        self.pages = pages
        self.completed = completed

    def mark_completed(self):
        """Toggle the book's completion status."""
        self.completed = not self.completed

    def is_long(self):
        """Return True if the book has more than 500 pages."""
        return self.pages > 500

    def to_dict(self):
        """Return book data as a dictionary for JSON saving."""
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "completed": self.completed
        }

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}, {self.pages} pages"
