import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager

# init SQLAlchemy for later use
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["DEBUG"] = True
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    app.config["MONGO_DBNAME"] = 'brew_master'
    app.config["MONGO_URI"] = 'mongodb+srv://root:rootbabyboy@honeycluster.v8y4e.mongodb.net/brew_master?retryWrites=true&w=majority'

    mongo = PyMongo(app)

    # blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
