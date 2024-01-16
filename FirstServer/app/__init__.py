from flask import Flask
from datetime import timedelta


def create_app():
    from .extensions import db, login_manager
    from auth import auth
    from main import main

    app = Flask(__name__, static_url_path='/static')

    app.config['SECRET_KEY']='Sjenwomew'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)

    login_manager.init_app(app)

    
    
    app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=3)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=40)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    with app.app_context():
        #db.drop_all()
        db.create_all()
    
    return app