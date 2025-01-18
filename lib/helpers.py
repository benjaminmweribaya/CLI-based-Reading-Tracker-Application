from lib.models import session
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_progress import ReadingProgress

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    User.add(name, email)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    total_pages = input("Enter total pages: ")
    Book.add(title, author, genre, total_pages)

def log_progress():
    try:
       user_id = int(input("Enter your user ID: "))
       book_id = int(input("Enter the book ID: "))
       pages_read = int(input("Enter pages read: "))
       reading_status = input("Enter status (To Read/Reading/Finished): ")
       ReadingProgress.log(user_id, book_id, pages_read, reading_status)

    except ValueError:
        print("Error: IDs and pages must be numbers!")

def view_books_by_status():
    """View books filtered by reading status along with user information."""
    status = input("Enter status to filter (To Read/Reading/Finished): ")
    ReadingProgress.view_by_status(status)

def calculate_percentage():
    """Calculate percentage completion for a user's books."""
    user_id = input("Enter your user ID: ")
    ReadingProgress.calculate_percentage(user_id)

def search_books():
    """Search for books by title or author."""
    search_term = input("Enter title or author to search for: ").lower()
    Book.search(search_term)

def sort_books():
    """Sort books by genre, title, or completion percentage."""
    print("Sort books by: 1) Title, 2) Genre, or 3) Completion Percentage")
    choice = input("> ")
    Book.sort(choice)

def delete_user():
    """Delete a user by ID."""
    try:
        user_id = int(input("Enter the user ID to delete: "))
        User.delete_by_id(user_id)
    except ValueError:
        print("Error: User ID must be a number.")

def delete_book():
    """Delete a book by ID."""
    try:
        book_id = int(input("Enter the book ID to delete: "))
        Book.delete_by_id(book_id)
    except ValueError:
        print("Error: Book ID must be a number.")

def delete_reading_progress():
    """Delete a reading progress record by ID."""
    try:
        progress_id = int(input("Enter the reading progress ID to delete: "))
        ReadingProgress.delete_by_id(progress_id)
    except ValueError:
        print("Error: Progress ID must be a number.")

def exit_program():
    print("Goodbye!")
    exit()
