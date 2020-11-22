from flask import jsonify, request

from . import api_a
from .main import func_main

AUTH_KEY = "1234ABCD"


@api_a.route("/api-a/<num>", methods=["GET"])
def view(num):

    # auth
    headers = request.headers
    auth = headers.get("X-Api-Key")

    # Auth
    if auth != AUTH_KEY:
        return jsonify({"error": "unauthorized"}), 401

    try:
        d = func_main(num)

    except Exception as e:
        print(e)
        d = {"a": num, "b": None, "c": None}

    return jsonify(d), 200
