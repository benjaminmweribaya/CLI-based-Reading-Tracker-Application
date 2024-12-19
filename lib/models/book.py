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
