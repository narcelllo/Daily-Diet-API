from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    diets = db.relationship('Diet', backref='user')
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')

class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, nullable=False)
    diet = db.Column(db.Boolean, nullable=False, default=True)
