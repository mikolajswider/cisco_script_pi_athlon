#!/usr/bin/env python

import json
import os
import subprocess
import time
import spark
import requests
import datetime

def old_url():
    l=[]
    with open ("/home/pi/pi-athlon/server/ngrok_url.txt", 'r') as f:
        for line in f:
            l.append(line.rstrip('\n'))
    f.close()
    return l

def new_url():
    l=[]
    data_file = requests.get("http://localhost:4040/api/tunnels")
    data = json.loads(data_file.text)
    url = data["tunnels"][0]["public_url"]
    if 'http://' in url:
        l.append(url[7:])
    else:
        l.append(url[8:])
    return l

def main():
    room_id = spark.mgs3x_room_id()
    token = spark.mgs3x_token()
    webhook_Id = spark.pi_athlon_c2_wbhook_id()
    oldurl=old_url()
    newurl=new_url()
    
    if oldurl!=newurl:
        #spark.update_webhook(token,webhook_Id, newurl[0])
        spark.message(room_id, token, newurl[0])
        with open ("/home/pi/pi-athlon/server/ngrok_url.txt", 'w') as f:
            f.write(newurl[0])
        f.close()
    
    
if __name__ == '__main__':
    main()