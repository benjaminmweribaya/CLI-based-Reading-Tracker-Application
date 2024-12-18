# Reading Tracker CLI Application

## Description
A command-line interface (CLI) application to help users manage their book collection and track reading progress.

## Features
1. Add users and books to the database.
2. Log and update reading progress for books.
3. Filter books by reading status (To Read, Reading, Finished).
4. Calculate percentage completion of books.
5. Search for books by title or author.
6. Sort books by title, genre, or completion percentage.

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pipenv install
   ```
3. Run the database setup:
   ```bash
   python lib/models/init_db.py
   ```
4. Run the CLI:
   ```bash
   python lib/cli.py
   ```

## Usage
Follow the prompts in the CLI to navigate and use the application effectively.

---
