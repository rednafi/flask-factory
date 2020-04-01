from flask import Blueprint

api_b = Blueprint(
    "api_b", __name__, template_folder="templates", static_folder="static"
)

from . import views  # isort:skip
