from flask import (jsonify, abort, request, make_response)
from app import auth, db
from app.api import bp_api
from app.models import User


# ------------------------------------- USER APIs ---------------------------------- #
@bp_api.route('/v1.0/users', methods=['GET'])
@auth.login_required
def get_users():
    """ ENDPOINT: /api/v1.0/users
    """
    _users = User.query.all()

    # SERIALIZE MODELS
    _users_list = []
    for user in _users:
        _users_list.append({
            'id': user.id,
            'username': user.username
        })

    # WE SERIALIZE AND RETURN LIST INSTEAD OF MODELS 
    return jsonify({'users': _users_list})


@bp_api.route('/v1.0/users/<int:id>', methods=['GET'])
@auth.login_required
def get_user(id):
    """ ENDPOINT: /api/v1.0/users/<user_id>
    """

    _user = User.query.get_or_404(id)
    if _user is None:
        abort(404)
    
    return jsonify({
        'id': _user.id,
        'username': _user.username})


@bp_api.route('/v1.0/users', methods=['POST'])
@auth.login_required
def create_user():
    """ ENDPOINT: /api/v1.0/users/
    """

    if not request.json:
        abort(404)
    
    if not 'username' in request.json and type(request.json['username']) != str:
        abort(404)

    if not 'password' in request.json:
        abort(404)
    
    _username = request.json['username']
    _password = request.json['password']
    _user = User(_username,_password)
    
    db.session.add(_user)
    db.session.commit()

    return jsonify({
        'id': _user.id,
        'username': _user.username
    })


@bp_api.route('/v1.0/user/<int:id>', methods=['PUT'])
@auth.login_required
def update_user(id):

    _user = User.query.get_or_404(id)
    
    if _user is None:
        abort(404)
    
    if not request.json:
        abort(404)

    if not 'username' in request.json and type(request.json['username']) != str:
        abort(404)

    _username = request.json['username']
    _user.username = _username
    db.session.commit()

    return jsonify({
        'id': _user.id,
        'username': _user.username
    })


@bp_api.route("/v1.0/user/<int:id>", methods=["DELETE"])
@auth.login_required
def delete_user(id):
    _user = User.query.get_or_404(id)

    if _user is None:
        abort(404)

    db.session.delete(value)
    db.session.commit()

    return jsonify({
        "Result": True
        })
# ------------------------------------- END USER APIs ---------------------------------- #