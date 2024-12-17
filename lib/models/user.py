from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    reading_progresses = relationship("ReadingProgress", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"