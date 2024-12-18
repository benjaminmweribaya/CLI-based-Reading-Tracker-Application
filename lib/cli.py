from lib.models import session
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_progress import ReadingProgress
from lib.helpers import add_user, add_book, log_progress, view_books_by_status, calculate_percentage, search_books, sort_books, exit_program

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_user()
        elif choice == "2":
            add_book()
        elif choice == "3":
            log_progress()
        elif choice == "4":
            view_books_by_status()
        elif choice == "5":
            calculate_percentage()
        elif choice == "6":
            search_books()
        elif choice == "7":
            sort_books()
        else:
            print("Invalid choice")

def menu():
    print("\nWelcome to the Reading Tracker CLI!")
    print("1. Add a new user")
    print("2. Add a new book")
    print("3. Log reading progress")
    print("4. View books by reading status")
    print("5. Calculate percentage completion for books")
    print("6. Search for books")
    print("7. Sort books")
    print("0. Exit the program")

if __name__ == "__main__":
    main()