from .service import *
from .forms import TransactionForm
from flask import Blueprint
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.before_request
def require_login():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

@transactions_bp.route('/')
def history():
    user = session.get('user_id')
    categories, error = get_expense_categories()

    filters = {
        "search": request.args.get("search", "").strip(),
        "category": request.args.get("category", "").strip(),
        "type": request.args.get("type", "").strip(),
        "sort": request.args.get("sort", "newest"),
        "page": request.args.get("page", 1, type=int)
    }

    data = get_transaction_history(user, filters)

    if error:
        flash(category="danger", message="Something went wrong")

    return render_template('transactions/history.html', data=data, categories=categories, title="Transactions")
   

@transactions_bp.route('/new', methods=("GET", "POST"))
def save_transaction():
    user = session.get('user_id')
    categories, error = get_expense_categories()

    if request.method == "POST":
        form = TransactionForm(request.form)

        if not form.validate():
            flash(category="danger", message="Invalid input")
            return render_template("transactions/create.html", title="New Transaction", form=form, categories=categories)
        
        description = form.description.data
        amount = form.amount.data
        type = form.type.data
        category = form.category.data
        transaction_date = form.transaction_date.data

        transaction, error = register_transaction(description, amount, category, user_id=user, date=transaction_date, tx_type=type)

        if transaction:
            flash("Your transaction has been saved!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash(category="danger", message=f"Error saving transaction: {error}")
            return render_template("transactions/create.html", title="New Transaction", form=form, categories=categories)

    # If the request method is GET
    form = TransactionForm()
    return render_template("transactions/create.html", title="New Transaction", form=form, categories=categories)

@transactions_bp.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    transaction, error = get_transaction(id)
    if transaction is None:
        error = 'Transaction not found!'
        flash(category='warning', message=error)
    
    if error:
        return redirect(url_for('transactions.history'))
    
    remove_transaction(id)
    
    # Flash a success message and redirect to the index page
    flash(category='success', message='Transaction deleted successfully!')
    return redirect(url_for('transactions.history'))

