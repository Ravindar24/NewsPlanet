from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class SubscriptionForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')