from datetime import datetime
from .repository import get_user_aggregate_data


def get_dashboard_data(user_id):
    transactions = get_user_aggregate_data(user_id)

    start_month = start_of_current_month()

    current_month = [
        t for t in transactions
        if datetime.fromisoformat(t["transaction_date"]) >= start_month
    ]

    income_month = sum(
        t["amount"] for t in current_month
        if t["type"] == "income"
    )

    expense_month = sum(
        t["amount"] for t in current_month
        if t["type"] == "expense"
    )

    saved_month = income_month - expense_month

    monthly_expenses = {}

    for t in transactions:
        if t["type"] != "expense":
            continue

        tx_date = datetime.fromisoformat(t["transaction_date"])

        key = (tx_date.year, tx_date.month)

        if key not in monthly_expenses:
            monthly_expenses[key] = 0

        monthly_expenses[key] += t["amount"]

    avg_monthly_spend = (
        sum(monthly_expenses.values()) / len(monthly_expenses)
        if monthly_expenses else 0
    )

    category_breakdown = get_category_breakdown(transactions)

    return {
        "income_month": income_month,
        "expense_month": expense_month,
        "saved_month": saved_month,
        "avg_monthly_spend": avg_monthly_spend,
        "currency": transactions[0]["currency"],
        "category_breakdown": category_breakdown,
    }


def start_of_current_month():
    now = datetime.now()

    return now.replace(
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )


def get_category_breakdown(transactions):
    category_totals = {}
    total_spend = 0

    for t in transactions:
        if t["type"] != "expense":
            continue

        key = t["category_name"]

        if key not in category_totals:
            category_totals[key] = {
                "name": t["category_name"],
                "icon": t["category_icon"],
                "total": 0
            }

        category_totals[key]["total"] += t["amount"]
        total_spend += t["amount"]

    breakdown = []

    for category in category_totals.values():
        category["percentage"] = (
            category["total"] / total_spend * 100
            if total_spend else 0
        )

        breakdown.append(category)

    breakdown.sort(key=lambda c: c["total"], reverse=True)

    return breakdown