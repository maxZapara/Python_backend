from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from app.extensions import db

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