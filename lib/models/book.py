from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

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