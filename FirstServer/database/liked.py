from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from app.extensions import db

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