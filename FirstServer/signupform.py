from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.widgets import TextArea

class CommentForm(FlaskForm):
    content=StringField('Comment', validators=[
        DataRequired(),
        Length(min=5, max=200)],
        widget=TextArea())
