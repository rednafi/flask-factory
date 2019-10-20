from flask import Blueprint

api_1 = Blueprint(
    "api_1", __name__, template_folder="templates", static_folder="static"
)

from . import views

