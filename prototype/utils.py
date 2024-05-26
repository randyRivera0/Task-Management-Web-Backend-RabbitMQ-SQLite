import os, sqlite3

import os
import sqlite3

def connect_to_db(db_name='tasks.db', db_folder='prototype'):
    """
    Connect to the SQLite database.

    Parameters:
        db_name (str): Name of the database file.
        db_folder (str): Relative path to the folder containing the database file.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    # Get the current working directory
    cwd = os.getcwd()
    # Define the path to the database file relative to the current working directory
    db_path = os.path.join(cwd, db_folder, db_name)
    # Connect to the database
    conn = sqlite3.connect(db_path)
    return conn
