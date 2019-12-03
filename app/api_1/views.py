from flask import jsonify
from flask import request
from app.api_1.module_main import func_main
from . import api_1

AUTH_KEY = "1234ABCD"


@api_1.route("/api_1/<num>", methods=["GET"])
def get_main_func(num):

    # auth
    headers = request.headers
    auth = headers.get("X-Api-Key")

    # Auth
    if auth != AUTH_KEY:
        return jsonify({"error": "unauthorized"}), 200

    try:
        d = func_main(num)

    except Exception as e:
        print(e)
        d = {"a": num, "b": None, "c": None}

    return jsonify(d), 200
