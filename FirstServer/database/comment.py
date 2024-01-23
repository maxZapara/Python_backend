from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from app.extensions import db

class Comment(db.Model,UserMixin):
   id: Mapped[int] = mapped_column(Integer, primary_key=True)
   content: Mapped[str] = mapped_column(String, nullable=False)
   movie_id: Mapped[int] = mapped_column(Integer)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  