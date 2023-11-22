from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms import StringField, PasswordField, EmailField, BooleanField
class RegistrForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=5, max=20)])
    email = EmailField('Email', validators=[
        DataRequired(),
        Email(),
        Regexp(r"^\S+@\S+\.\S+$", message='Bad email address')]) 
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, max=25),
        Regexp(r"(?=.*[a-z])(?=.*[A-Z]+)(?=.*\d)(?=.*[!@#$%&._])(?=.*[a-zA-Z\d]){4,}", message='Bad password')])
    checkbox = BooleanField('I Agree to Privacy Policy')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=5, max=20)]) 
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, max=25),
        Regexp(r"(?=.*[a-z])(?=.*[A-Z]+)(?=.*\d)(?=.*[!@#$%&._])(?=.*[a-zA-Z\d]){4,}", message='Bad password')])
    checkbox = BooleanField('I Agree to Privacy Policy')