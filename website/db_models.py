from . import db
from flask_login import UserMixin

class users(db.Model, UserMixin):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    files = db.Column(db.String(5000))

    def __init__(self, name, password, email, files):
        self.password = password
        self.name = name
        self.email = email
        self.files = files
