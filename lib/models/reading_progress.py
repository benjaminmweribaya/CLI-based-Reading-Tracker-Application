from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from . import Base
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
