from lib.models import session
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_progress import ReadingProgress
from lib.helpers import (
    add_user, 
    add_book, 
    log_progress, 
    view_books_by_status, 
    calculate_percentage, 
    search_books, 
    sort_books, 
    delete_user,
    delete_book,
    delete_reading_progress,
    exit_program
)

# Menu options as a list of tuples
MENU_OPTIONS = [
    (0, "Exit the program", exit_program),
    (1, "Add a new user", add_user),
    (2, "Add a new book", add_book),
    (3, "Log reading progress", log_progress),
    (4, "View books by reading status", view_books_by_status),
    (5, "Calculate percentage completion for books", calculate_percentage),
    (6, "Search for books", search_books),
    (7, "Sort books", sort_books),
    (8, "Delete a user", delete_user),
    (9, "Delete a book", delete_book),
    (10, "Delete a reading progress", delete_reading_progress),
]

def display_menu():
    """Display menu options."""
    print("\nWelcome to the Reading Tracker CLI!")
    for option, description, _ in MENU_OPTIONS:
        print(f"{option}. {description}")


def menu():
    while True:
        display_menu()
        try:
            choice = int(input("> "))
            # Use a dictionary to map choices to functions
            menu_dict = {option: action for option, _, action in MENU_OPTIONS}
            if choice in menu_dict:
                menu_dict[choice]()  # Call the corresponding function
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    menu()