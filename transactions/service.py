from .repository import *
from datetime import datetime, timezone
import math

__all__ = [
    "register_transaction",
    "get_transaction",
    "get_expense_categories",
    "get_transaction_history",
    "remove_transaction"
]

CURRENCY_FACTORS = {
    "GBP": 100,   # pound -> pence
    "USD": 100,   # dollar -> cents
    "EUR": 100,   # euro -> cents
    "JPY": 1,
}

def get_transaction_history(user_id, filters, limit=10):
    page = filters["page"]

    if page < 1:
        page = 1

    offset = (page - 1) * limit

    rows, total = get_user_transactions(user_id, filters, limit, offset)

    total_pages = math.ceil(total / limit) if total else 1

    income_total = sum(
        t["amount"] for t in rows if t["type"] == "income"
    )

    expense_total = sum(
        t["amount"] for t in rows if t["type"] == "expense"
    )

    net_total = income_total - expense_total

    return {
        "transactions": rows,
        "page": page,
        "total_pages": total_pages,
        "total_transactions": total,
        "income_total": income_total,
        "expense_total": expense_total,
        "net_total": net_total
    }


def get_expense_categories():
    try:
        categories = get_categories()
        return categories, None
    
    except Exception as error:
        return None, str(error)
    
def get_transaction(id):
    try:
        transaction = get_transaction(id)
        return transaction, None
    
    except Exception as error:
        return None, str(error)

def register_transaction(description, amount, category, user_id, date, currency="GBP", tx_type="expense"):
    try:
        tx_amount = money_to_minor_unit(amount, currency)
        tx_date = parse_date(date)
        transaction = create_transaction(description, tx_amount, category, user_id, currency, tx_type, transaction_date=tx_date.isoformat())
        return transaction, None
    
    except Exception as error:
        return None, str(error)
    
def remove_transaction(id):  
    delete_transaction(id)
  

def money_to_minor_unit(amount, currency):
    factor = CURRENCY_FACTORS.get(currency, 100)
    return round(float(amount) * factor)


def parse_date(value):
    return datetime.fromisoformat(value)
