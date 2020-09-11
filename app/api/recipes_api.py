from flask import (jsonify, abort, request, make_response)
from app import auth
from app.api import bp_api
from app.models import Recipe


# ------------------------------------- RECIPES APIs ---------------------------------- #

@bp_api.route('/v1.0/recipes', methods=['GET'])
@auth.login_required
def get_recipes():
    """ ENDPOINT: /api/v1.0/recipes
    """
    _recipes = Recipe.query.all()

    # SERIALIZE MODELS
    _recipes_list = []
    for recipe in _recipes:
        _recipes_list.append({
            'id': recipe.id,
            'name': recipe.name
        })

    # WE SERIALIZE AND RETURN LIST INSTEAD OF MODELS 
    return jsonify({'recipes': _recipes_list})


@bp_api.route('/v1.0/recipes/<int:id>', methods=['GET'])
@auth.login_required
def get_recipe(id):
    """ ENDPOINT: /api/v1.0/recipes/<recipe_id>
    """

    _recipe = Recipe.query.get_or_404(id)
    if not _recipe:
        abort(404)
    
    return jsonify({
        'id': _recipe.id,
        'username': _recipe.name})


@bp_api.route('/v1.0/recipes', methods=['POST'])
@auth.login_required
def create_recipe():
    """ ENDPOINT: /api/v1.0/recipes/
    """

    if not request.json:
        abort(404)
    
    if not 'name' in request.json:
        abort(404)
    
    pass