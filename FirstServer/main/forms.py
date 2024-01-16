from wtforms import StringField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm

class CommentForm(FlaskForm):
    content=StringField('Comment', validators=[
        DataRequired(),
        Length(min=5, max=200)],
        widget=TextArea())