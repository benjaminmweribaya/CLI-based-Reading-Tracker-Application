from lib.models import session
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_progress import ReadingProgress

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if session.query(User).filter_by(email=email).first():
        print("Error: User with this email already exists!")
    else:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print("User added successfully!")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    total_pages = input("Enter total pages: ")
    try:
        total_pages = int(total_pages)
        book = Book(title=title, author=author, genre=genre, total_pages=total_pages)
        session.add(book)
        session.commit()
        print("Book added successfully!")
    except ValueError:
        print("Error: Total pages must be a number!")

def log_progress():
    try:
       user_id = int(input("Enter your user ID: "))
       book_id = int(input("Enter the book ID: "))
       pages_read = int(input("Enter pages read: "))
       reading_status = input("Enter status (To Read/Reading/Finished): ")

       # Validate user and book exist
       user = session.query(User).filter_by(id=user_id).first()
       book = session.query(Book).filter_by(id=book_id).first()

       if not user:
           print("Error: User does not exist!")
           return
       if not book:
           print("Error: Book does not exist!")
           return
       if pages_read > book.total_pages:
           print("Error: Pages read cannot exceed total pages!")
           return

        # Log or update progress
       progress = session.query(ReadingProgress).filter_by(user_id=user_id, book_id=book_id).first()
       if progress:
           progress.pages_read = pages_read
           progress.reading_status = reading_status
           print("Progress updated successfully!")
       else:
           progress = ReadingProgress(user_id=user_id, book_id=book_id, pages_read=pages_read, reading_status=reading_status)
           session.add(progress)
           print("Progress logged successfully!")

       session.commit()
       
    except ValueError:
        print("Error: IDs and pages must be numbers!")

def view_books_by_status():
       """View books filtered by reading status along with user information."""
       status = input("Enter status to filter (To Read/Reading/Finished): ")
       progresses = session.query(ReadingProgress).filter_by(reading_status=status).all()
       if progresses:
           print(f"Books with status '{status}':")
           for progress in progresses:
               book = session.query(Book).filter_by(id=progress.book_id).first()
               user = session.query(User).filter_by(id=progress.user_id).first()
               print(f"- {book.title} by {book.author} | Pages Read: {progress.pages_read}/{book.total_pages} | User: {user.name} (ID: {user.id})")
       else:
           print("No books found for this status.")

def calculate_percentage():
    """Calculate percentage completion for a user's books."""
    user_id = input("Enter your user ID: ")
    try:
        user_id = int(user_id)
        progresses = session.query(ReadingProgress).filter_by(user_id=user_id).all()
        if not progresses:
            print("No reading progress found for this user.")
            return
        for progress in progresses:
            book = session.query(Book).filter_by(id=progress.book_id).first()
            percentage = (progress.pages_read / book.total_pages) * 100
            print(f"{book.title} by {book.author} | {percentage:.2f}% Completed")
    except ValueError:
        print("Error: User ID must be a number.")

def search_books():
    """Search for books by title or author."""
    search_term = input("Enter title or author to search for: ").lower()
    books = session.query(Book).all()
    results = [book for book in books if search_term in book.title.lower() or search_term in book.author.lower()]
    if results:
        for book in results:
            print(f"{book.title} by {book.author} | Genre: {book.genre}")
    else:
        print("No matching books found.")

def sort_books():
    """Sort books by genre, title, or completion percentage."""
    print("Sort books by: 1) Title, 2) Genre, or 3) Completion Percentage")
    choice = input("> ")
    if choice == "1":
        books = session.query(Book).order_by(Book.title).all()
    elif choice == "2":
        books = session.query(Book).order_by(Book.genre).all()
    elif choice == "3":
        books = session.query(Book).all()
        books = sorted(books, key=lambda b: calculate_completion_percentage(b), reverse=True)
    else:
        print("Invalid choice!")
        return

    for book in books:
        print(f"{book.title} by {book.author} | Genre: {book.genre}")

def calculate_completion_percentage(book):
    """Helper to calculate completion percentage for sorting."""
    progress = session.query(ReadingProgress).filter_by(book_id=book.id).first()
    if progress:
        return (progress.pages_read / book.total_pages) * 100
    return 0

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
