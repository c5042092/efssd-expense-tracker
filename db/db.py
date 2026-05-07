import sqlite3
import os

# Establish connection to the SQLite database
def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file
    DB_PATH = os.path.join(BASE_DIR, 'database.db') # Construct the full path to the database file
    conn = sqlite3.connect(DB_PATH)                 # Connect to the database
    conn.row_factory = sqlite3.Row                  # Enable dictionary-like access to rows
    return conn