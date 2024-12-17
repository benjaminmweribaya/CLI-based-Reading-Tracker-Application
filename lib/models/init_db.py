from lib.models import Base, engine
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_progress import ReadingProgress

if __name__ == "__main__":
    print("Creating database...")
    Base.metadata.create_all(engine)
    print("Database created!")