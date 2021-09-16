import os
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.sqlite3"
UPLOAD_FOLDER = 'uploads/'
ALLOWED_ENDINGS =   ["txt", "md", "json", "jar",
                    "png", "jpg", "jpeg", "gif",
                    "mp3", "wav", "mp4", "avi",
                    "apk", "pdf", "doc", "docx", "ppt", "pptx",
                    "zip", "rar", "tar", "iso",
                    "py", "cpp", "c", "cs", "java"]

def crate_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = "Z9OSHcwYASPwlj3"
    app.permanent_sesion_lifetime = timedelta(days=1)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)

    from .accounts import accounts
    from .files import files
    from .db_models import users

    app.register_blueprint(accounts, url_prefix='/account')
    app.register_blueprint(files, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return users.query.get(int(id))


    return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)


