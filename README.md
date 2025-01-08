# Reading Tracker CLI Application

## Description
The Reading Tracker CLI Application is a Python-based command-line interface (CLI) tool designed to help users manage their book collection, track their reading progress, and organize their reading habits effectively. This application uses SQLAlchemy as the ORM to handle database interactions seamlessly.

## Features
1. **User Management**:
   - Add new users to the system.
   - View a list of all users.
   - Delete users from the database.
2. **Book Management**:
   - Add new books to the database.
   - Search for books by title or author.
   - Sort books by title, genre, or completion percentage.
   - Delete books from the database.
3. **Reading Progress Tracking**:
   - Log and update reading progress for books.
   - View books filtered by reading status (To Read, Reading, Finished).
   - Calculate percentage completion for books.
   - Delete reading progress records.
4. **CLI Navigation**:
   - Intuitive menu system with options for all major features.
   - Input validation to ensure user-friendly error handling.

## Setup
### Prerequisites
- Python 3.8 or higher
- Pipenv for managing dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/benjaminmweribaya/CLI-based-Reading-Tracker-Application
   cd CLI-based-Reading-Tracker-Application
   ```
2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
4. Install the project in the virtual environment
   ```bash
   pip install -e .
   ```

### Database Initialization
Run the following script to set up the SQLite database:
```bash
python lib/models/init_db.py
```
This will create a `reading_tracker.db` file in the project directory.

### Running the Application
Launch the CLI application:
```bash
python lib/cli.py
```

## Usage
Once the CLI is running, follow the on-screen prompts to interact with the application. The main menu provides the following options:
1. Add a new user.
2. Add a new book.
3. Log or update reading progress.
4. View books by reading status.
5. Calculate percentage completion for books.
6. Search for books by title or author.
7. Sort books.
8. Delete a user.
9. Delete a book.
10. Delete a reading progress.
0. Exit the application.

## Project Structure
```
CLI-based-Reading-Tracker-Application/
├── .venv/                       # Virtual environment (optional, can be regenerated)
├── lib/
│   ├── __pycache__/             # Compiled Python files (can be ignored)
│   ├── __init__.py              # Marks lib as a Python package
│   ├── cli.py                   # Main CLI logic
│   ├── debug.py                 # Debugging utilities
│   ├── helpers.py               # Helper functions for CLI operations
│   ├── models/                  # Contains ORM models and database setup
│   │   ├── __pycache__/         # Compiled Python files for models (can be ignored)
│   │   ├── __init__.py          # Database initialization
│   │   ├── user.py              # User model
│   │   ├── book.py              # Book model
│   │   ├── reading_progress.py  # ReadingProgress model
│   │   ├── init_db.py           # Script to initialize the database
├── reading_tracker_cli.egg-info # Metadata for the Python package (auto-generated)
├── .gitignore                   # Git ignore rules
├── LICENSE                      # License information
├── Pipfile                      # Pipenv dependencies
├── Pipfile.lock                 # Dependency lock file
├── reading_tracker.db           # SQLite database file
├── README.md                    # Project documentation
├── setup.py                     # Installation script

```

## Technologies Used
- **Python**: Core programming language.
- **SQLite**: Lightweight database for data storage.

## Author
**Mr. Benjamin Mweri Baya**  
Email: [b3njaminbaya@gmail.com](mailto:b3njaminbaya@gmail.com)  
GitHub: [benjaminmweribaya](https://github.com/benjaminmweribaya)  

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Feel free to contribute or reach out for any feedback or suggestions!

