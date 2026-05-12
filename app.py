from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf
import os
from dotenv import load_dotenv
from auth.routes import auth
from transactions.routes import transactions_bp
from dashboard.routes import dashboard

load_dotenv()

app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(transactions_bp, url_prefix="/transactions")
app.register_blueprint(dashboard, url_prefix="/dashboard")

siteName = "Pennywise"
# Set the site name in the app context
@app.context_processor
def inject_site_name():
    return dict(siteName=siteName)

@app.context_processor
def inject_currency_symbols():
    return dict(
        CURRENCY_SYMBOLS={
            "GBP": "£",
            "USD": "$",
            "EUR": "€",
            "JPY": "¥"
        }
    )

secret = os.getenv("SECRET_KEY")
app.secret_key = secret

csrf = CSRFProtect(app)
# Create the csrf_token global variable
@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())

@app.route('/')
def index():
    return render_template('index.html', title="Welcome")

# Run application
if __name__ == '__main__':
    print("Starting application...")
    print("The application is running on http://localhost:4000")
    app.run(host='0.0.0.0', port=4000, debug=True)