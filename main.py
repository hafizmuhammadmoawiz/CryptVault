import subprocess
import os
import sys

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def start_application():

    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the SQLite database and tables on first run, if it doesn't exist yet.
    db_path = os.path.join(current_directory, "database", "database.db")
    if not os.path.exists(db_path):
        sys.path.insert(0, current_directory)
        from database.db_manager import create_database

        create_database()

    login_page = os.path.join(current_directory, "gui", "login_page.py")

    subprocess.run(["python", login_page])


if __name__ == "__main__":

    start_application()
