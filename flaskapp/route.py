from flaskapp import *
from flask import render_template
from flaskapp.models import *
from flaskapp.module import *

@app.route("/")
def home():
    return render_template("home.html")
