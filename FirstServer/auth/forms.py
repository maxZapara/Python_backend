from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from wtforms import StringField, PasswordField, EmailField, BooleanField

def validate_username(form, username):
    from database import User
    user=User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError("username already in use")
    
def validate_email(form, email):
    from database import User
    user=User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError("email already in use")


class RegistrForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=5, max=20),
        validate_username])
    email = EmailField('Email', validators=[
        DataRequired(),
        Email(),
        Regexp(r"^\S+@\S+\.\S+$", message='Bad email address'),
        validate_email]) 
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