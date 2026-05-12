# Example transactions data for testing
transactions_data = [
    {
        "description": "Salary - May",
        "amount": 3500,
        "currency": "GBP",
        "type": "income",
        "user": 1,
        "category": None,
        "transaction_date": "2026-05-02"
    },
    {
        "description": "Groceries - Tesco",
        "amount": 564,
        "currency": "GBP",
        "type": "expense",
        "user": 1,
        "category": 6,  # Groceries
        "transaction_date": "2026-05-03"
    },
    {
        "description": "Uber ride",
        "amount": 149,
        "currency": "GBP",
        "type": "expense",
        "user": 1,
        "category": 3,  # Transport
        "transaction_date": "2026-05-04"
    },
    {
        "description": "Freelance payment",
        "amount": 6000,
        "currency": "GBP",
        "type": "income",
        "user": 1,
        "category": None,
        "transaction_date": "2026-05-06"
    },
    {
        "description": "Netflix subscription",
        "amount": 129,
        "currency": "GBP",
        "type": "expense",
        "user": 1,
        "category": 4,  # Bills & Utilities (better fit than Health)
        "transaction_date": "2026-05-07"
    },
    {
        "description": "Coffee - Starbucks",
        "amount": 125,
        "currency": "GBP",
        "type": "expense",
        "user": 1,
        "category": 2,  # Food
        "transaction_date": "2026-05-08"
    },
    {
        "description": "Stock dividend",
        "amount": 1200,
        "currency": "GBP",
        "type": "income",
        "user": 1,
        "category": None,
        "transaction_date": "2026-05-09"
    },
    {
        "description": "Gym membership",
        "amount": 250,
        "currency": "GBP",
        "type": "expense",
        "user": 1,
        "category": 5,  # Health
        "transaction_date": "2026-05-10"
    }
]