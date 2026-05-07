from .repository import *
from werkzeug.security import check_password_hash, generate_password_hash

__all__ = [
    "validate_login",
    "register_user"
]

def validate_login(email, password):
    user = get_user_by_email(email)
    if user and check_password_hash(user["password"], password):
        return user
    return None

def register_user(first_name, last_name, email, password):
    # Check if user record exists
    if get_user_by_email(email):
        return None, "A user with that email is already registered!"

    first_name = normalize_name(first_name)
    last_name = normalize_name(last_name)
    password_hash = generate_password_hash(password)

    # Create new user record
    user = create_user(first_name, last_name, email, password_hash)

    return user, None

def normalize_name(name):
    return name.strip().capitalize()
