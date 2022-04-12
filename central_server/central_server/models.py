from central_server import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    update_time = db.Column(db.DateTime)
