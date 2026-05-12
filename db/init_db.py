import sqlite3
from werkzeug.security import generate_password_hash
from test_data import transactions_data

# This script should be run once to set up the database schema and initial data
# Database will be created in the same directory as this script and named 'database.db'
connection = sqlite3.connect('database.db')
# This opens the schema.sql file and executes its contents to create the necessary tables
with open('schema.sql') as f:
    connection.executescript(f.read())
# Create a cursor object to execute SQL commands
cur = connection.cursor()
# Insert initial data into the user table
cur.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
            ('John', 'Doe', 'test@example.com', generate_password_hash('Password123'))
            )

# Create default expense categories

cur.executemany(
    "INSERT INTO categories (name, icon) VALUES (?, ?)",
    [
        ('Rent & Housing', '🏠'),
        ('Food', '🍽️'),
        ('Transport', '🚗'),
        ('Bills & Utilities', '🧾'),
        ('Health', '🩺'),
        ('Groceries', '🛒'),
        ('Others', '📦')
    ]
) 

# Create transactions based on transaction_data in test_data.py
for transaction in transactions_data:
        cur.execute(
        """
        INSERT INTO transactions
        (description, amount, currency, type, user, category, transaction_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            transaction["description"],
            transaction["amount"],
            transaction["currency"],
            transaction["type"],
            transaction["user"],
            transaction["category"],
            transaction["transaction_date"]
        )
    )

# Commit the changes to the database and close the connection
connection.commit()
connection.close()
