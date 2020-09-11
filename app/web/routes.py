from flask import render_template, redirect
from . import bp_web


@bp_web.route('/')
def index():
    return render_template('web/index.html')