from flask import Blueprint

api_2 = Blueprint(
    "api_2", __name__, template_folder="templates", static_folder="static"
)

from . import views
