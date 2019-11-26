from flask import Flask, request
from flask import Response
from flask_cors import CORS
import RPi.GPIO as GPIO
import json


app = Flask(__name__)
cors = CORS(app, resource={r"/v1/*": {"origins": "*"}})
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
led = GPIO.PWM(7, 100)

def setValue(val):
    led.start(0)
    led.ChangeDutyCycle(int(val))
        


@app.route('/', methods=['GET'])
def message():
    message = {'message': 'Slider API'}
    data = json.dumps(message)
    resp = Response(data, status=200, mimetype='application/json')
    return resp

@app.route('/v1/ping', methods=['GET'])
def checkService():
    message = {'result': 'pong'}
    data = json.dumps(message)
    resp = Response(data, status=200, mimetype='application/json')
    return resp

@app.route('/v1/led-change', methods=['POST'])
def changeLed():
    data = request.get_json()
    if type(data['value']) == int:
        if data['value'] >= 0:
            setValue(data['value'])
            message = {'result': 'changing!'}
            data_resp = json.dumps(message)
            resp = Response(data_resp, status=201, mimetype='application/json')
            return resp
        else:
            message = {'result': 'The value must be a positive'}
            data = json.dumps(message)
            resp = Response(data, status=400, mimetype='application/json')
            return resp
    else:
        message = {'result': 'The value must be an integer'}
        data = json.dumps(message)
        resp = Response(data, status=400, mimetype='application/json')
        return resp
