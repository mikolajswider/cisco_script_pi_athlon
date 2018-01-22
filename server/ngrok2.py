#!/usr/bin/env python

import json
import os
import subprocess
import time
import spark
import requests
import urllib3

def sendGET(url):
    content = requests.get(url)
    return content

def sendgett(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    return response

def start():
    subprocess.call('/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/launch_ngrok.sh')
    
def provide_url():
    http_url=''
    https_url=''
    #data_file = os.system("curl  http://localhost:4040/api/tunnels")
    data_file = sendGET("http://localhost:4040/api/tunnels")
    #print (str(data_file.text))
    data = json.loads(data_file.text)
    url = data["tunnels"][0]["public_url"]
    print (url)