from central_server.models import User
from central_server import db
from datetime import datetime


def user_add(username: str, ip_address: str):
    user = User()
    user.user_name = username
    user.ip = ip_address
    user.create_time = datetime.now()
    user.update_time = datetime.now()
    db.session.add(user)
    db.session.commit()
    return "Successfully add new user"


def user_get(username: str):
    user = User.query.filter_by(user_name=username).first()
    if user is None:
        return "No such user found! "
    body = {'id': user.id,
            'username': user.user_name,
            'ip': user.ip
            }
    return body


def user_update(username: str, ip: str):
    user = User.query.filter_by(user_name=username).first()
    user.ip = ip
    db.session.commit()
    return "Successfully updated new user"
