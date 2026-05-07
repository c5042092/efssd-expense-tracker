from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    first_name = StringField(validators=[DataRequired(), Length(max=30)])
    last_name = StringField(validators=[DataRequired(), Length(max=30)])

    email = StringField(validators=[DataRequired(), Email()])

    password = PasswordField(validators=[DataRequired(), Length(min=6)])

    confirm_password = PasswordField(
        validators=[DataRequired(), EqualTo("password", message="Passwords must match")]
    )