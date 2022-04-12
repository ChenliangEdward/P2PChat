from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '9a60237f4c33bbf2d6e8ed639740770d271abc6ebc5908c6dc72e42871d45ae0'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///central.db'
db = SQLAlchemy(app)

from central_server import routes