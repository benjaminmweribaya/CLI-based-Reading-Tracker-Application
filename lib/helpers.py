from lib.models import session
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_progress import ReadingProgress

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print("User added successfully!")


def exit_program():
    print("Goodbye!")
    exit()
