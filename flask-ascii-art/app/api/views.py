from . import api
from flask import jsonify
from flask import request
from .main_func import draw_ascii
from .ascii_art import text

AUTH_KEY = "1234"


@api.route("/ascii-art/", defaults={"text": text})
@api.route("/ascii-art/<text>", methods=["GET"])
def get_ascii_drawing(text):

    # auth
    headers = request.headers
    auth = headers.get("X-Api-Key")

    # Auth
    if auth != AUTH_KEY:
        return jsonify({"error": "unauthorized"}), 200

    d = draw_ascii(text)

    return d, 200              # jsonify(d) is another option when exporting dictionary
