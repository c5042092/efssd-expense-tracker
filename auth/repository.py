from db.db import get_db_connection

__all__ = [
    'create_user',
    'get_user_by_email'
]

def create_user(first_name, last_name, email, password_hash):
    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (?, ?, ?, ?)
        """,
        (first_name, last_name, email, password_hash)
    )
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    return user