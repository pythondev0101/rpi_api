from flask import Flask, jsonify, make_response, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_httpauth import HTTPBasicAuth
from multiprocessing import Process, Queue
from config import app_config
from app.arduino import Arduino


db = SQLAlchemy()
auth = HTTPBasicAuth()
qLEDStatus = Queue()
arduino = Arduino()
login_manager = LoginManager()


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'bp_web.login'

    with app.app_context():
        # START MULTIPROCESSING
        arduino_process = Process(target=arduino.test_process, args=(qLEDStatus,))
        arduino_process.start()

        @app.errorhandler(404)
        def not_found(error):
            return make_response(jsonify({"error": "Not found"}), 404)

        @app.before_request
        def before_request():
            g.user = current_user

        @app.route('/')
        def index():
            return redirect(url_for('bp_web.login'))

        """ REGISTER BLUEPRINT (Project Module) """
        from . import api, web

        app.register_blueprint(api.bp_api)
        app.register_blueprint(web.bp_web)

        db.create_all()
        db.session.commit()
        init_db()

    return app


def init_db():
    from .models import User, Pick
    import csv
    import platform
    from config import basedir


    if User.query.count() == 0:
        admin = User("admin", "admin")
        db.session.add(admin)
        db.session.commit()
        print("Initial user.......success")
    
    if Pick.query.count() == 0:
        if platform.system() == "Windows":
            csv_path = basedir + "\\app" + "\\picklist.csv"
        elif platform.system() == "Linux":
            csv_path = basedir + "/app/picklist.csv"
        else:
            raise Exception("Invalid OS")
        
        with open(csv_path) as f:
            csv_file = csv.reader(f)
            for id,row in enumerate(csv_file):
                if not id == 0:
                    p = Pick()
                    p.number = row[0]
                    p.barcode = row[1]
                    db.session.add(p)
            db.session.commit()
            
        print("Insert picklist.......success")
