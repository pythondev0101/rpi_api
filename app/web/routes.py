from flask import render_template, redirect
from . import bp_web
from app.models import Pick, Recipe


@bp_web.route('/')
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