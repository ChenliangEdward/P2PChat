from flaskapp import db


class Friends(db.Model):
    username = db.Column(db.String(38), unique=True, primary_key=True)
    ip = db.Column(db.String(30))


class Messages(db.Model):
    timestamp = db.Column(db.Integer, unique=True, primary_key=True)
    from_name = db.Column(db.String)
    to_name = db.Column(db.String)
