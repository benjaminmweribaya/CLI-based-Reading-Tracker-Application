import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///reading_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
