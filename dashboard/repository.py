from db.db import get_db_connection

def get_user_aggregate_data(user_id):
    conn = get_db_connection()
    transactions = conn.execute("""
        SELECT
            t.amount,
            t.type,
            t.currency,
            t.transaction_date,
            c.name AS category_name,
            c.icon AS category_icon
        FROM transactions t
        LEFT JOIN categories c ON t.category = c.id
        WHERE t.user = ?
    """, (user_id,)).fetchall()
    
    # categories = conn.execute( """
    #     SELECT *
    #     FROM categories
    #     ORDER BY name ASC
    # """).fetchall()

    conn.close()

    return transactions
