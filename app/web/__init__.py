from flask import render_template, redirect, Blueprint
from app import auth


bp_web = Blueprint('bp_web',__name__, url_prefix='/web',template_folder='templates',\
     static_folder='static', static_url_path='/web/static') 


from . import routes