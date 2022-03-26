from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisIsARandomGeneratedHardCodedSecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note  # or just state 'import .models' -> this latter doesn't work in this context. may want to investigate why
  

    #create db if needed
    create_database(app)

    return app

#check if db already exists, if not: create it    
def create_database (app):
    if not path.exists('website/' + DB_NAME ):
        db.create_all(app=app)
        print('DAtabase created!')