from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from lib.models import Base, session
from datetime import datetime

class ReadingProgress(Base):
    __tablename__ = 'reading_progresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    pages_read = Column(Integer, default=0)
    reading_status = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reading_progresses")
    book = relationship("Book", back_populates="reading_progresses")

    def __repr__(self):
        return f"<ReadingProgress(user_id={self.user_id}, book_id={self.book_id}, pages_read={self.pages_read}, status={self.reading_status})>"

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
