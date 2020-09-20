from flask import (Blueprint, jsonify, abort, request, make_response)
from werkzeug.security import generate_password_hash, check_password_hash
from app import auth
from app.models import User


bp_api = Blueprint('bp_api', __name__, url_prefix='/api')


# ------------------------------------- IMPORT ALL APIS ---------------------------------- #
from . import users_api, recipes_api, leds_api
# ------------------------------------- END IMPORT ALL APIS ---------------------------------- #
