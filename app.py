from flask import Flask, request
import json
import logging

from werkzeug.exceptions import BadRequestKeyError

SERVICE_DEBUG = True
app = Flask(__name__)

users = []
id_counter = 0


@app.route('/')
def hello_world():
    return 'Students api'


@app.route("/users/<id_user>", methods=['GET'])
def user_by_id(id_user):
    for user in users:
        if user['id'] == int(id_user):
            return user, 200
    return {}, 404


@app.route('/users', methods=['GET', 'POST'])
def users_route():
    if request.method == "GET":
        return {"users": users}, 200
    elif request.method == "POST":
        try:
            global id_counter
            user = {
                "ime": request.json["ime"],
                "username": request.json.get("username"),
                "ocena": request.json.get("ocena"),
                "id": id_counter
            }
            id_counter += 1
            logging.info("New user: " + json.dumps(user))
            users.append(user)
            return user, 201
        except (BadRequestKeyError, Exception, TypeError) as e:
            logging.error(e)
            return {"error": str(e)}, 429


if __name__ == '__main__':
    app.run(host="localhost", port=8081, debug=False)
