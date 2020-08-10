#!/usr/bin/env python
#  
#  
from flask import  Flask, render_template, request, url_for
import os
from dotenv import load_dotenv
from twilio.rest import Client
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

load_dotenv()

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
TOKEN = os.environ.get('TOKEN')
FROM = os.environ.get('FROM')
TO = os.environ.get('TO')

@app.route('/', methods=['POST', 'GET'])
def led():
    if request.method == 'POST':
        client = Client(ACCOUNT_SID, TOKEN)
        if request.form.get("turnOnBtn"):
            GPIO.output(18, GPIO.HIGH)
            print("Led successfully turned on")
            msg = client.messages.create(
                body='Lights ON',
                from_=FROM,
                to=TO)
            print(msg.sid)
        if request.form.get("turnOffBtn"):
            GPIO.output(18, GPIO.LOW)
            print("Led successfully turned off")
            msg = client.messages.create(
                body='Lights OFF',
                from_=FROM,
                to=TO)
            print(msg.sid)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    
