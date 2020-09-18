from flask import (jsonify, abort, request, make_response)
from app import auth, db
from app.api import bp_api



@bp_api.route('/v1.0/leds', methods=['GET'])
@auth.login_required
def get_leds():
    """ ENDPOINT: /api/v1.0/leds
    """

    _leds_list = []
    
    for id, pin in LEDS.items():
        _status = GPIO.input(pin)

        _leds_list.append({
            'id': id,
            'status': _status,
        })

    return jsonify({
        'leds': _leds_status_list
    })


@bp_api.route('/v1.0/leds/<int:id>', methods=['GET'])
@auth.login_required
def get_led(id):
    """ ENDPOINT: /api/v1.0/leds/<id>
    """
    if id not in LEDS:
        abort(404)

    _led = LEDS[id]
    _status = GPIO.input(_led)

    return jsonify({
        'id': id,
        'pin': _led,
        'status': _status
        })


@bp_api.route('/v1.0/control-led/<int:id>')
@auth.login_required
def control_led(id):
    """ ENDPOINT: /api/v1.0/control-led/<id>
    """

    if id not in LEDS:
        abort(404)
    
    if not request.json:
        abort(400)
    
    _state = request.json['']
    GPIO.output(LEDS[id],)

