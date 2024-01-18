import os
from datetime import timedelta
from dotenv import load_dotenv

class Config():
    def __init__(self):
        load_dotenv()
        self.SECRET_KEY=os.getenv('SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        self.REMEMBER_COOKIE_DURATION=timedelta(days=int(os.getenv('REMEMBER_COOKIE_DURATION')))
        self.PERMANENT_SESSION_LIFETIME=timedelta(days=int(os.getenv('PERMANENT_SESSION_LIFETIME')))