from flask import Blueprint

api_a = Blueprint(
    "api_a", __name__, template_folder="templates", static_folder="static"
)

from . import views  # isort:skip
