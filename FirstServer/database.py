# from flask_login import UserMixin
# from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import LoginManager
from flask_login import UserMixin

login_manager = LoginManager()

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(db.Model,UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String,unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    liked_movies = db.relationship('Likes', backref='user')
    comments = db.relationship('Comment', backref='user')
    def __str__(self):
       return f"User: {self.username}"
    def __repr__(self):
       return f"User: {self.username}"
    
class Likes(db.Model,UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[str] = mapped_column(Numeric, nullable=False)
    poster_path: Mapped[str] = mapped_column(String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __str__(self):
       return f"Movie: {self.title}"
    def __repr__(self):
       return f"Movie: {self.title}"
    
class Comment(db.Model,UserMixin):
   id: Mapped[int] = mapped_column(Integer, primary_key=True)
   #date: Mapped[str] = mapped_column(String, nullable=False)
   content: Mapped[str] = mapped_column(String, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   movie_id: Mapped[int] = mapped_column(Integer)