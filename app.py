from flask import Flask
from flask_wtf import CSRFProtect

# load .env in development only
if os.environ.get("FLASK_ENV") == "development":
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

app = Flask(__name__)

siteName = "SHU Cash Tracker"
# Set the site name in the app context
@app.context_processor
def inject_site_name():
    return dict(siteName=siteName)

secret = os.environ.get("SECRET_KEY")
if not secret:
    raise RuntimeError("SECRET_KEY is not set")

app.secret_key = secret

csrf = CSRFProtect(app)
# Create the csrf_token global variable
@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())

@app.route('/')
def index():
    return "Hello World!"

# Run application
if __name__ == '__main__':
    print("Starting application...")
    print("The application is running on http://localhost:4000")
    app.run(host='0.0.0.0', port=4000, debug=True)