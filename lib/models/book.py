from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base, session

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    total_pages = Column(Integer, nullable=False)
    reading_progresses = relationship("ReadingProgress", back_populates="book", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, genre={self.genre})>"
    
    @classmethod
    def add(cls, title, author, genre, total_pages):
        """Add a new book with validation."""
        # Validate the title
        if not title or title.isdigit():
            print("Error: Book title must not be empty or just numbers!")
            return

        # Validate the author
        if not author or author.isdigit():
            print("Error: Author name must not be empty or just numbers!")
            return

        # Validate the genre
        if not genre:
            print("Error: Genre cannot be empty!")
            return

        # Validate total pages
        try:
            total_pages = int(total_pages)
            if total_pages <= 0:
                print("Error: Total pages must be a positive number!")
                return
        except ValueError:
            print("Error: Total pages must be a number!")
            return

        # Add the book to the database
        if session.query(cls).filter_by(title=title, author=author).first():
            print("Error: A book with this title and author already exists!")
            return

        book = cls(title=title, author=author, genre=genre, total_pages=total_pages)
        session.add(book)
        session.commit()
        print("Book added successfully!")


    @classmethod
    def search(cls, search_term):
        """Search for books by title or author."""
        books = session.query(cls).all()
        results = [book for book in books if search_term in book.title.lower() or search_term in book.author.lower()]
        if results:
            for book in results:
                print(f"{book.title} by {book.author} | Genre: {book.genre}")
        else:
            print("No matching books found!")

    @classmethod
    def sort(cls, choice):
        """Sort books by title, genre, or completion percentage."""
        if choice == "1":
            books = session.query(cls).order_by(cls.title).all()
        elif choice == "2":
            books = session.query(cls).order_by(cls.genre).all()
        else:
            print("Invalid choice!")
            return

        for book in books:
            print(f"{book.title} by {book.author} | Genre: {book.genre}")
    
    @classmethod
    def delete_by_id(cls, book_id):
        """Delete a book by its ID."""
        try:
           book = session.query(cls).filter_by(id=book_id).first()
           if book:
               session.delete(book)
               session.commit()
               print(f"Book with ID {book_id} deleted successfully!")
           else:
               print(f"No book found with ID {book_id}.")
        except Exception as e:
            print(f"An error occurred while deleting the book: {e}")
