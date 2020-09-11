from flask import render_template, redirect, Blueprint


bp_web = Blueprint('bp_web',__name__, url_prefix='/web',template_folder='templates') 

from . import routes