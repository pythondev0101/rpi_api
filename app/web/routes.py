from flask import render_template, redirect, request, url_for, make_response, jsonify, g
from flask_login import current_user, login_user, logout_user, login_required
from . import bp_web
from app.models import User, Pick, Recipe
from app import auth, login_manager


# ------------------------------------- AUTHENTICATION ---------------------------------- #
def _custom_login(username, password):
    user = g.user
    return user

@auth.verify_password
def verify_password(username, password):
    return _custom_login(username, password)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error": "Unauthorized access"}), 401)
# ------------------------------------- END AUTHENTICATION ---------------------------------- #


@bp_web.route('/')
@login_required
def index():
    _pick_model = Pick.query.all()
    _pick_list = [[]]
    ctr = 0
    row = 0

    for i in _pick_model:

        if not ctr == 4:
            _pick_list[row].append(i)
            ctr += 1
        else:
            row += 1
            _pick_list.append([])
            _pick_list[row].append(i)
            ctr = 1
    
    _recipes = Recipe.query.all()

    return render_template('web/index.html',picklist=_pick_list,recipes=_recipes)


@bp_web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('bp_web.index'))
            
        return render_template('web/login.html')

    elif request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']

        user = User.query.filter_by(username=_username).first()

        if user is not None and user.check_password(_password) is not None:
            login_user(user)
            return redirect(url_for('bp_web.index'))
        else:
            return redirect(url_for('bp_web.login'))

@bp_web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bp_web.login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)