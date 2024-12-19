from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base, session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    reading_progresses = relationship("ReadingProgress", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
    @classmethod
    def delete_by_id(cls, user_id):
        """Delete a user by their ID."""
        try:
           user = session.query(cls).filter_by(id=user_id).first()
           if user:
               session.delete(user)
               session.commit()
               print(f"User with ID {user_id} deleted successfully!")
           else:
               print(f"No user found with ID {user_id}.")
        except Exception as e:
            print(f"An error occurred while deleting the user: {e}")