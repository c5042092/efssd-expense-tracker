from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError

class RegisterForm(FlaskForm):
    first_name = StringField(validators=[DataRequired(), Length(min=3, max=30, message="First Name must be between 3 and 30 characters.")])
    last_name = StringField(validators=[DataRequired(), Length(min=3, max=30, message="Last Name must be between 3 and 30 characters.")])

    email = StringField(validators=[DataRequired(), Email()])

    password = PasswordField(
        validators=[
            DataRequired(),
            Length(min=8),
            Regexp(
                r"^(?=.*[A-Z])(?=.*\d).+$",
                message=(
                    "Password must contain "
                    "an uppercase letter and number."
                ),
            ),
        ]
    )

    confirm_password = PasswordField(
        validators=[DataRequired(), EqualTo("password", message="Passwords must match")]
    )