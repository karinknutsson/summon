from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=True)
    startDate = db.Column(db.DateTime(), nullable=False)
    endDate = db.Column(db.DateTime(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text())

    def __init__(self, url, startDate, endDate, name, description):
        self.url = url
        self.startDate = startDate
        self.endDate = endDate
        self.name = name
        self.description = description

    def __repr__(self):
        return '<id {}>'.format(self.id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<id {}>'.format(self.id)
