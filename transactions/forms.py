from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, Optional, AnyOf

class TransactionForm(FlaskForm):
    description = StringField(
        validators=[
            DataRequired(),
            Length(
                min=3,
                max=255,
                message="Description must be between 3 and 255 characters."
            )
        ]
    )

    amount = DecimalField(
        validators=[
            DataRequired(),
            NumberRange(min=0.01)
        ]
    )

    currency = StringField(
        default="GBP",
        validators=[
            Optional(),
            Length(min=3, max=3)
        ]
    )

    type = StringField(
        validators=[
            DataRequired(),
            AnyOf(["income", "expense"])
        ]
    )

    category = IntegerField(validators=[DataRequired()])

    transaction_date = StringField(validators=[DataRequired()])

