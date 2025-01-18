from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from lib.models import Base, session
from lib.models.user import User  
from lib.models.book import Book
from datetime import datetime

class ReadingProgress(Base):
    __tablename__ = 'reading_progresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    pages_read = Column(Integer, default=0)
    reading_status = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="reading_progresses")
    book = relationship("Book", back_populates="reading_progresses")

    def __repr__(self):
        return f"<ReadingProgress(user_id={self.user_id}, book_id={self.book_id}, pages_read={self.pages_read}, status={self.reading_status})>"
    

    @classmethod
    def log(cls, user_id, book_id, pages_read, reading_status):
        """Log or update reading progress."""
        user = session.query(User).filter_by(id=user_id).first()
        book = session.query(Book).filter_by(id=book_id).first()
        if not user:
            raise ValueError("Error: User does not exist!")
        if not book:
            raise ValueError("Error: Book does not exist!")
        if pages_read > book.total_pages:
            raise ValueError("Error: Pages read cannot exceed total pages!")

        progress = session.query(cls).filter_by(user_id=user_id, book_id=book_id).first()
        if progress:
            progress.pages_read = pages_read
            progress.reading_status = reading_status
            print("Progress updated successfully!")
        else:
            progress = cls(user_id=user_id, book_id=book_id, pages_read=pages_read, reading_status=reading_status)
            session.add(progress)
            print("Progress logged successfully!")
        session.commit()

    @classmethod
    def view_by_status(cls, status):
        """View books filtered by reading status."""
        progresses = (
            session.query(cls)
            .join(Book)
            .join(User)
            .filter(cls.reading_status == status)
            .all()
        )
        if progresses:
            print(f"Books with status '{status}':")
            for progress in progresses:
                print(f"- {progress.book.title} by {progress.book.author} | Pages Read: {progress.pages_read}/{progress.book.total_pages} | User: {progress.user.name} (ID: {progress.user.id})")
        else:
            print("No books found for this status.")

    @classmethod
    def calculate_percentage(cls, user_id):
        """Calculate percentage completion for a user's books."""
        progresses = session.query(cls).filter_by(user_id=user_id).all()
        if not progresses:
            print("No reading progress found for this user.")
            return
        for progress in progresses:
            if progress.book.total_pages == 0:
               print(f"{progress.book.title} by {progress.book.author} | Total pages is zero. Cannot calculate percentage.")
               continue
            percentage = (progress.pages_read / progress.book.total_pages) * 100
            print(f"{progress.book.title} by {progress.book.author} | {percentage:.2f}% Completed")

    @classmethod
    def delete_by_id(cls, progress_id):
        """Delete a reading progress record by its ID."""
        try:
           progress = session.query(cls).filter_by(id=progress_id).first()
           if progress:
               session.delete(progress)
               session.commit()
               print(f"Reading progress with ID {progress_id} deleted successfully!")
           else:
               print(f"No reading progress found with ID {progress_id}.")
        except Exception as e:
            print(f"An error occurred while deleting the reading progress: {e}")
