from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base, session
import re

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    reading_progresses = relationship("ReadingProgress", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    

    @classmethod
    def create(cls, name, email):
        """Validate and create a new user."""
        if not cls.validate_name(name):
            print("Error: Name must contain only alphabetic characters.")
            return None
        if not cls.validate_email(email):
            print("Error: Invalid email format.")
            return None

        if session.query(cls).filter_by(email=email).first():
            print("Error: User with this email already exists!")
            return None

        user = cls(name=name, email=email)
        session.add(user)
        session.commit()
        print("User created successfully!")
        return user

    @staticmethod
    def validate_name(name):
        """Ensure the name contains only alphabetic characters."""
        return bool(re.match(r'^[a-zA-Z\s]+$', name))

    @staticmethod
    def validate_email(email):
        """Ensure the email is valid."""
        # Match basic email format: letters/numbers before '@', domain name, and extension.
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
    
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