"""
CP1404 Assignment 1 - Books to Read (Improved Version for Assignment 2)
Name: Roshik Maharjan
Date Started: 20/10/2025
GitHub URL: https://github.com/Roshik-hub/a1-books-Roshik-hub.git

"""

FILENAME = "books.csv"

MENU = """Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
>>> """


def main():
    """Run the Books to Read program."""
    print("Books to Read 1.0 by Roshik Maharjan")
    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.")

    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'd':
            display_books(books)
        elif choice == 'a':
            add_book(books)
        elif choice == 'c':
            complete_book(books)
        else:
            print("Invalid menu choice")
        choice = input(MENU).lower()

    save_books(FILENAME, books)
    print(f"{len(books)} books saved to {FILENAME}")
    print('"So many books, so little time. Frank Zappa"')


def load_books(filename):
    """
    Load book data from a CSV file.

    Returns:
        list: List of books, each in format [title, author, pages, status].
    """
    books = []
    with open(filename, "r") as in_file:
        for line in in_file:
            title, author, pages, status = line.strip().split(",")
            books.append([title, author, int(pages), status])
    return books


def save_books(filename, books):
    """Save the list of books back to the CSV file."""
    with open(filename, "w") as out_file:
        for title, author, pages, status in books:
            print(f"{title},{author},{pages},{status}", file=out_file)


def display_books(books):
    """Display all books, highlighting unread ones."""
    unread_count = 0
    unread_pages = 0

    for i, book in enumerate(books, 1):
        mark = "*" if book[3] == 'u' else " "
        print(f"{mark}{i}. {book[0]} by {book[1]} {book[2]} pages")

        if book[3] == 'u':
            unread_count += 1
            unread_pages += book[2]

    if unread_count == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still need to read {unread_pages} pages in {unread_count} books.")


def add_book(books):
    """Add a new book after validating all fields."""
    title = input("Title: ").strip()
    while not title:
        print("Input can not be blank")
        title = input("Title: ").strip()

    author = input("Author: ").strip()
    while not author:
        print("Input can not be blank")
        author = input("Author: ").strip()

    pages_input = input("Number of Pages: ").strip()
    pages = get_valid_page_count(pages_input)

    books.append([title, author, pages, 'u'])
    print(f"{title} by {author} ({pages} pages) added.")


def get_valid_page_count(initial):
    """Validate and return a positive integer for page count."""
    pages_input = initial
    while True:
        try:
            pages = int(pages_input)
            if pages > 0:
                return pages
            print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")
        pages_input = input("Number of Pages: ").strip()


def complete_book(books):
    """Mark a book as completed after validating the selected number."""
    unread_books = [b for b in books if b[3] == 'u']

    if not unread_books:
        print("No unread books - well done!")
        return

    for i, book in enumerate(books, 1):
        mark = "*" if book[3] == 'u' else " "
        print(f"{mark}{i}. {book[0]} by {book[1]} {book[2]} pages")

    unread_pages = sum(book[2] for book in unread_books)
    print(f"You still need to read {unread_pages} pages in {len(unread_books)} books.")

    index = get_valid_book_number(books)
    if index is not None:
        books[index][3] = 'c'
        print(f"{books[index][0]} by {books[index][1]} completed!")


def get_valid_book_number(books):
    """Get a valid unread book number from user and return its index."""
    while True:
        user_input = input("Enter the number of a book to mark as completed\n>>> ").strip()

        try:
            number = int(user_input)
            if number < 1:
                print("Number must be > 0")
            elif number > len(books):
                print("Invalid book number")
            elif books[number - 1][3] == 'c':
                print("That book is already completed")
            else:
                return number - 1
        except ValueError:
            print("Invalid input - please enter a valid number")


if __name__ == "__main__":
    main()
