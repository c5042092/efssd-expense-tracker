from flask import Blueprint, session, render_template, url_for, redirect
from .service import get_dashboard_data

dashboard = Blueprint("dashboard", __name__)

@dashboard.before_request
def require_login():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

@dashboard.route('/', methods=("GET",))
def user_dashboard():
    user = session.get("user_id")

    transactions_data = get_dashboard_data(user)

    return render_template('dashboard.html', title="Dashboard", data=transactions_data)