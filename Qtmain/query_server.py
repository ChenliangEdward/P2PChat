import requests
import json

basepath = "http://127.0.0.1:5000"


def user_Post(username, ip):
    url = basepath + "/user/add"
    payload = {'username': username,
               'ip': ip}
    response = requests.request("POST", url, headers={}, data=payload)
    return response.status_code


def user_Get(username):
    url = basepath + f"/user/get?username={username}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def user_Patch(username, ip):
    url = basepath + "/user/update"

    payload = {'username': username,
               'ip': ip}
    files = [

    ]
    headers = {}

    response = requests.request("PATCH", url, headers=headers, data=payload, files=files)

    print(response.text)

# print(json.loads(user_Get("test123"))["ip"])
