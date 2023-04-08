from flask import Flask, jsonify
from flask import request
from model import recommend_workout
from flask_cors import CORS

flask_app = Flask(__name__)
CORS(flask_app)


@flask_app.route("/", methods=["GET"])
def get():
    return "Flask app is working!"


@flask_app.route("/recommend_workout", methods=["POST", "GET"], strict_slashes=False)
def recommend():
    if request.method == "POST":
        try:
            print(request)
            request_data = request.get_json()
            print(request_data)
            response = recommend_workout(request_data)
            return jsonify(response)
        except Exception as e:
            return "ERROR: " + str(e)

    if request.method == "GET":
        return "THIS IS A MESSAGE FROM /recommend_workout GET"


if __name__ == "__main__":
    flask_app.run()