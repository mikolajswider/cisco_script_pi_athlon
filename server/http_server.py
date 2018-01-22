#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, request
from datetime import datetime
import os, traceback, sys 
import json
import os
import challenge_2
import leds

app = Flask('__name__')

@app.route('/',methods=['GET','POST','OPTIONS'])                                                                                                                                         

def listen_to_spark():
    start = "mgs3X_RoBot: start"
    stop = "mgs3X_RoBot: stop"
    token = 'YWU0OTQxMDEtZTIyYi00MmI3LWJkNjgtODljZTkwZDMzNTg5MTc1MGJhN2YtYzk4'  # mgs3X-RoBot Authorization token
    room_Id = 'Y2lzY29zcGFyazovL3VzL1JPT00vYTUyYzMxMjAtNWNmMS0xMWU3LTkxZmEtMTUxNjVhZmMzYWZh'
    room_mgs3x = 'Y2lzY29zcGFyazovL3VzL1JPT00vMWQ3ZDg4YjAtNWMxZS0xMWU3LWIzNTktYTVhMGJkZjcyMTJm'
    zmienna = 0

    data = request.get_data()

    for word in data:
        if word == start:
            zmienna = 1
    if zmienna==1:
        leds.green_led_on()
        return "Challenge 2 in progress..."
    else:
        return "No challenge in progress."
         
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=5000)