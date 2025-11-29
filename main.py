"""
Main Kivy App for Assignment 2 - CP1404

Author: Roshik Maharjan
Date: 28/11/2025
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty
from bookcollection import BookCollection
from books import Book

BOOKS_FILE = "books.json"

class ReadingTrackerApp(App):
    """Main Application Class."""
    status_top = StringProperty()
    status_bottom = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection = BookCollection()

    def build(self):
        self.title = "Reading Tracker 2.0"
        self.collection.load_books(BOOKS_FILE)
        self.update_top_status()
        return self.root

    def on_stop(self):
        """Save books on exit."""
        self.collection.save_books(BOOKS_FILE)

    def update_top_status(self):
        """Update top label: pages left to read."""
        pages = self.collection.get_pages_to_read()
        self.status_top = f"Pages to read: {pages}"

    def clear_inputs(self):
        """Clear input fields."""
        self.root.ids.title_input.text = ""
        self.root.ids.author_input.text = ""
        self.root.ids.pages_input.text = ""
        self.status_bottom = ""

    def handle_add_book(self):
        """Add a book with validation."""
        title = self.root.ids.title_input.text.strip()
        author = self.root.ids.author_input.text.strip()
        pages = self.root.ids.pages_input.text.strip()

        if not title or not author or not pages:
            self.status_bottom = "Please complete all fields."
            return

        try:
            pages = int(pages)
        except ValueError:
            self.status_bottom = "Please enter a valid number"
            return

        if pages <= 0:
            self.status_bottom = "The book must have some pages!"
            return

        new_book = Book(title, author, pages, False)
        self.collection.add_book(new_book)
        self.clear_inputs()
        self.update_top_status()
        self.create_book_buttons()
        self.status_bottom = f"Added {title}"

    def handle_sort(self, value):
        """Sort books using spinner selection."""
        key_map = {
            "Title": "title",
            "Author": "author",
            "Pages": "pages"
        }
        self.collection.sort_books(key_map[value])
        self.create_book_buttons()

    def create_book_buttons(self):
        """Display book buttons dynamically."""
        container = self.root.ids.books_box
        container.clear_widgets()

        for book in self.collection.books:
            color = (0.5, 1, 0.5, 1) if book.completed else (1, 0.7, 0.7, 1)
            btn = Button(
                text=f"{book.title} ({book.author}) - {book.pages} pages",
                background_color=color,
                on_release=lambda b, book=book: self.toggle_book(book)
            )
            container.add_widget(btn)

    def toggle_book(self, book):
        """Toggle completion state."""
        book.completed = not book.completed
        message = "You completed a long book!" if book.is_long() else "Completed!"
        self.status_bottom = f"{book.title}: {message}" if book.completed else f"{book.title} set to unread"
        self.update_top_status()
        self.create_book_buttons()


ReadingTrackerApp().run()
