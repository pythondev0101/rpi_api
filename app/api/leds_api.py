from flask import (jsonify, abort, request, make_response)
from app import auth, db, arduino
from app.api import bp_api
from app import qLEDStatus


# ------------------------------------- LEDs APIs ---------------------------------- #

@bp_api.route('/v1.0/leds', methods=['GET'])
@auth.login_required
def get_leds():
    """ ENDPOINT: /api/v1.0/leds
    """
    
    _leds_status_list = qLEDStatus.get()

    return jsonify({
        'leds': _leds_status_list
    })


@bp_api.route('/v1.0/leds/<int:id>', methods=['GET'])
@auth.login_required
def get_led(id):
    """ ENDPOINT: /api/v1.0/leds/<id>
    """

    _leds_list = qLEDStatus.get()

    # Temporary lang to, dapat magrefer pa din sa id ng led
    # wag sa index ng list
    id -= 1

    return jsonify({
        'led':_leds_list[id]
    })
 

@bp_api.route('/v1.0/control-led/<int:id>', methods=['POST'])
@auth.login_required
def control_led(id):
    """ ENDPOINT: /api/v1.0/control-led/<id>
    """

    if not request.json:
        abort(400)

    if 'state' not in request.json:
        abort(400)
    
    # _state = request.json['state']

    # arduino.control_led(id, state)

    return jsonify({"result": True})
