from flask import Flask



def create_app():
    from .extensions import db, login_manager
    from auth import auth
    from main import main
    from config import Config

    app = Flask(__name__, static_url_path='/static')

    app.config.from_object(Config())

    db.init_app(app)

    login_manager.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    with app.app_context():
        #db.drop_all()
        db.create_all()
    
    return app