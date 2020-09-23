import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

# init SQLAlchemy for later use
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    app.config["MONGO_DBNAME"] = 'brew_master'
    app.config["MONGO_URI"] =  'mongodb+srv://root:rootbabyboy@honeycluster.v8y4e.mongodb.net/brew_master?retryWrites=true&w=majority'

    mongo = PyMongo(app)

    # blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
