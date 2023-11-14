from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length
class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=5, max=20)])
    email = EmailField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4, max=13)])