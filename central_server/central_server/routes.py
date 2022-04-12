from central_server.services import user_get, user_add, user_update
from central_server import app
from flask import request


@app.route("/")
def home():
    return "<h1>central server test page<h1>"


@app.route("/user/add", methods=['POST'])
def user_add_controller():
    username = request.form.get('username')
    ip = request.form.get('ip')
    return user_add(username, ip)


@app.route("/user/get")
def user_get_controller():
    username = request.args.get("username")
    return user_get(username)


@app.route("/user/update", methods=['PATCH'])
def user_update_controller():
    username = request.form.get("username")
    ip = request.form.get("ip")
    return user_update(username, ip)
