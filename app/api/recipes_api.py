from flask import (jsonify, abort, request, make_response)
from app import auth, db
from app.api import bp_api
from app.models import Recipe, RecipePick


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
        _picklist = []
        for pick in recipe.recipe_pick:
            _picklist.append(pick.id)

        _recipes_list.append({
            'id': recipe.id,
            'name': recipe.name,
            'picklist': _picklist
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
        abort(400)
    
    _picklist = []
    for pick in _recipe.recipe_pick:
        _picklist.append(pick.id)

    return jsonify({
        'id': _recipe.id,
        'name': _recipe.name,
        'picklist': _picklist
        })


@bp_api.route('/v1.0/recipes', methods=['POST'])
@auth.login_required
def create_recipe():
    """ ENDPOINT: /api/v1.0/recipes/
    """

    if not request.json:
        abort(400)
    
    if not 'name' in request.json:
        abort(400)
    
    if not 'picklist' in request.json:
        abort(400)
    
    _name = request.json['name']
    _picklist = request.json['picklist']

    recipe = Recipe()
    recipe.name = _name

    db.session.add(recipe)
    db.session.commit()

    ctr = 1
    for pick in _picklist:
        recipe_pick = RecipePick(
            recipe=recipe,
            pick_id=pick,
            order=ctr
        )
        ctr += 1
        
        db.session.add(recipe_pick)
        db.session.commit()
    
    return jsonify({
        'id': recipe.id,
        'name': recipe.name,
        'result': True
    })


# FOR TESTING

# PICK ID, PIN
LEDS = {
    '1': 'Pin No.', '2': 'Pin No.', '3': 'Pin No.', '4': 'Pin No.',
    '5': 'Pin No.','6': 'Pin No.', '7': 'Pin No.', '8': 'Pin No.',
    '9': 'Pin No.', '10': 'Pin No.','11': 'Pin No.', '12': 'Pin No.',
    '13': 'Pin No.', '14': 'Pin No.', '15': 'Pin No.','16': 'Pin No.',
    '17': 'Pin No.', '18': 'Pin No.', '19': 'Pin No.', '20': 'Pin No.',
    '21': 'Pin No.', '22': 'Pin No.', '23': 'Pin No.', '24': 'Pin No.',
    '25': 'Pin No.','26': 'Pin No.', '27': 'Pin No.', '28': 'Pin No.',
}

@bp_api.route('/v1.0/ledsstatus', methods=['GET'])
@auth.login_required
def get_led_status():
    import random
    """ ENDPOINT: /api/v1.0/ledsstatus
    """

    _leds_status_list = []
    
    for id, pin in LEDS.items():
        _status = random.randint(0,1)


        _leds_status_list.append({
            'id': id,
            'status': _status,
        })

    return jsonify({
        'leds_status': _leds_status_list
    })
