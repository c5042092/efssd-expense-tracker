from .service import *
from .forms import RegisterForm
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        print({"data": request.form})
        email = request.form['email']
        password = request.form['password']

        user = validate_login(email, password)

        if not user:
            flash("Invalid email or password!", "danger")
            return render_template("auth/login.html", title="Log In")

        session.clear()
        session["user_id"] = user["id"]

        flash(f"Welcome back {user['first_name']}!", "success")
        return redirect(url_for("index"))

    return render_template("auth/login.html", title="Log In")

@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method  == "POST":
        form = RegisterForm(request.form)

        if not form.validate():
            flash(category="danger", message="Invalid input")
            return render_template("auth/register.html", form=form)
        
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        user, error = register_user(first_name, last_name, email, password)

        if user:
            flash("Registration successful! Welcome!", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(category="danger", message=f"Registration failed: {error}")
            return render_template("auth/register.html", form=form)

    # If the request method is GET
    form = RegisterForm()
    return render_template("auth/register.html", title="Register", form=form)

@auth.route("/logout")
def logout():
    session.clear()
    flash(category='info', message='You have been logged out.')
    return redirect(url_for('index'))