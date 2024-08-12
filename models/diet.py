from datetime import datetime
from database import db

class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    consistent_diet = db.Column(db.Boolean, nullable=False, default=True)
