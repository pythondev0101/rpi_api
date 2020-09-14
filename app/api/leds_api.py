from flask import (jsonify, abort, request, make_response)
from app import auth, db
from app.api import bp_api
import RPi.GPIO as GPIO



# ------------------------------------- RPI/LEDs CONFIGURATIONS ---------------------------------- #
GPIO.setmode(GPIO.BOARD)

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

# SETTING UP PINS TO OUT
for id, pin in LEDS.items():
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# ------------------------------------- LEDs APIs ---------------------------------- #

@bp_api.route('/v1.0/ledsstatus', methods=['GET'])
@auth.login_required
def get_led_status():
    """ ENDPOINT: /api/v1.0/ledsstatus
    """

    _leds_status_list = []
    
    for id, pin in LEDS.items():
        _status = GPIO.input(pin)

        _leds_status_list.append({
            'id': id,
            'status': _status,
        })

    return jsonify({
        'leds_status': _leds_status_list
    })

