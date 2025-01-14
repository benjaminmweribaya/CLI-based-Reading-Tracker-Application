import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///reading_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

from .user import User
from .book import Book
from .reading_progress import ReadingProgress