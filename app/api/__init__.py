from flask import (Blueprint, jsonify, abort, request, make_response)
from werkzeug.security import generate_password_hash, check_password_hash
from app import auth
from app.models import User


bp_api = Blueprint('bp_api', __name__, url_prefix='/api')


# ------------------------------------- AUTHENTICATION ---------------------------------- #
@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        return user


@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error": "Unauthorized access"}), 401)
# ------------------------------------- END AUTHENTICATION ---------------------------------- #


# ------------------------------------- IMPORT ALL APIS ---------------------------------- #
from . import users_api, recipes_api
# ------------------------------------- END IMPORT ALL APIS ---------------------------------- #
