from db.db import get_db_connection

__all__ = [
    "create_transaction",
    "get_transaction_by_id",
    "get_user_transactions",
    "delete_transaction",
    "get_categories"
]

def create_transaction(description, amount, category, user_id, currency, tx_type, transaction_date):
    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO transactions (description, amount, currency, type, user, category, transaction_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, 
        (description, amount, currency, tx_type, user_id, category, transaction_date)
    )
    conn.commit()
    conn.close()


def get_categories():
    conn = get_db_connection()
    categories = conn.execute("SELECT * FROM categories ORDER BY name ASC").fetchall()
    conn.close()
    return categories
    

def get_user_transactions(user_id, filters, limit, offset):
    conn = get_db_connection()

    query = """
        SELECT
            transactions.*,
            COUNT(*) OVER() AS total_count
        FROM transactions
        WHERE user = ?
    """

    params = [user_id]

    if filters.get("search"):
        query += " AND description LIKE ?"
        params.append(f"%{filters['search']}%")

    if filters.get("category"):
        query += " AND category = ?"
        params.append(filters["category"])

    if filters.get("type"):
        query += " AND type = ?"
        params.append(filters["type"])

    query += """
        ORDER BY transaction_date DESC
        LIMIT ? OFFSET ?
    """

    params.append(limit)
    params.append(offset)

    rows = conn.execute(query, params).fetchall()

    conn.close()

    total = rows[0]["total_count"] if rows else 0
    return rows, total
    

def get_transaction_by_id(tx_id):
    conn = get_db_connection()
    transaction = conn.execute("SELECT * FROM transactions WHERE id = ?", (tx_id,)).fetchone()
    conn.close()
    return transaction


def delete_transaction(tx_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
    conn.commit()
    conn.close()