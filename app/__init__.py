from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
auth = HTTPBasicAuth()


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    
    db.init_app(app)

    with app.app_context():
        @app.errorhandler(404)
        def not_found(error):
            return make_response(jsonify({"error": "Not found"}), 404)

        """ REGISTER BLUEPRINT (Project Module) """
        from . import api, web

        app.register_blueprint(api.bp_api)
        app.register_blueprint(web.bp_web)

        db.create_all()
        db.session.commit()
        init_db()

    return app


def init_db():
    from .models import User

    if db.session.query(User).count() == 0:
        admin = User("admin", "admin")
        db.session.add(admin)
        db.session.commit()
