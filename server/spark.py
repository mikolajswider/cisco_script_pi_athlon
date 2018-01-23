#!/usr/bin/env python

import datetime #set date and time
import requests #http messages
import time
import base64
import os #use linux commands
import subprocess
from requests_toolbelt.multipart.encoder import MultipartEncoder
import spark
import json


def mgs3x_token():
    return 'YWU0OTQxMDEtZTIyYi00MmI3LWJkNjgtODljZTkwZDMzNTg5MTc1MGJhN2YtYzk4'

def mgs3x_room_id():
    return 'Y2lzY29zcGFyazovL3VzL1JPT00vMWQ3ZDg4YjAtNWMxZS0xMWU3LWIzNTktYTVhMGJkZjcyMTJm'

def pi_athlon_room_id():
    return 'Y2lzY29zcGFyazovL3VzL1JPT00vNDU3Y2E5YTAtYmIxMy0xMWU3LWExNTgtZjNhOGIxZjBiYmUz'

def mgs3x_webhook_id():
    return 'Y2lzY29zcGFyazovL3VzL1dFQkhPT0svMmQ0NTY4OWQtNzNjMC00MGQyLWIwMGItZjg2ODhiZTk0Nzg0'


def start():
    token = spark.mgs3x_token()
    room_Id = spark.mgs3x_room_id()
    header = {
        'Authorization': 'Bearer ' + token}  # define the header which will allow mgs3X-Robot to communicate with Spark

    body = {"roomId": room_Id, "text": "Pi-Athlon Robot Metal Gear 3X - start time: " +time.strftime("%H:%M:%S")+" CET, "+time.strftime("%d/%m/%Y")}
    response = requests.post('https://api.ciscospark.com/v1/messages', data=body, headers=header)
    
def message(room_id, token, text):
    header = {
        'Authorization': 'Bearer ' + token}  # define the header which will allow mgs3X-Robot to communicate with Spark
    body = {"roomId": room_id, "text": "Pi-Athlon Robot Metal Gear 3X - "+text}
    response = requests.post('https://api.ciscospark.com/v1/messages', data=body, headers=header)

def list_files(path):
    '''
    Returns a list which elements are filenames of files that are in path.
    '''
    l=[]
    line=''
    output = os.popen('ls -1 '+ path).read()
    for char in output:
        if char == '\n':
            l.append(line)
            line=''
        else:
            line=line+char
    return l    

def finish():
    token = spark.mgs3x_token()
    room_Id = spark.mgs3x_room_id()
    url= 'https://api.ciscospark.com/v1/messages'
    path = '/home/pi/Pictures/pi_athlon/' # path to pictures
    
    #==================================================
    #Sending Finish Message to Spark
    #==================================================
    
    header1 = {
        'Authorization': 'Bearer ' + token}  # define the header which will allow mgs3X-Robot to communicate with Spark

    body1 = {"roomId": room_Id, "text": "Pi-Athlon Robot Metal Gear 3X - finish time: " +time.strftime("%H:%M:%S")+" CET, "+time.strftime("%d/%m/%Y")}
    response1  = requests.post('https://api.ciscospark.com/v1/messages', data=body1, headers=header1)

    
    #==================================================
    #Sending Pictures to Spark
    #==================================================
    picture_list=list_files(path)
    i=1
    for picture in picture_list:
        path_file=path+picture
        multipart_data = MultipartEncoder(
            fields={
                # a file upload field
                'files': (picture, open(path_file, 'rb'), 'image/jpg'),
                # plain text fields
                'text': 'Picture '+str(i), 
                'roomId': room_Id,
                })
        header={'Authorization': 'Bearer ' + token, 'Content-Type': multipart_data.content_type}  # define the header which will allow mgs3X-Robot to communicate with Spark
        #body={"roomId": test_room_Id, "text": "Pi-Athlon Robot Metal Gear 3X - finish time: " +time.strftime("%H:%M:%S")+" CET, "+time.strftime("%d/%m/%Y")
        response = requests.post(url, headers=header, data=multipart_data)
        i=i+1
        command="sudo rm "+path+picture
        os.system(command)
        
def update_webhook(token,webhook_Id,url):
    header = {"Accept" : "application/json","Content-Type":"application/json","Authorization": "Bearer " + token}  # define the header which will allow mgs3X-Robot to communicate with Spark
    body = {"targetUrl": url}
    body = json.dumps(body)#body needs to be a sring
    response = requests.put('https://api.ciscospark.com/v1/webhooks/'+webhook_Id, data=body, headers=header)
'''
def sendSparkGET(url):
    headers={"Accept" : "application/json", "Content-Type":"application/json", "Authorization" : "Bearer "+ webhookToken }
    data = requests.get(url, headers=headers).json()
    return data

def sendSparkPOST(url, data):
    headers={"Accept" : "application/json", "Content-Type":"application/json", "Authorization" : "Bearer "+ webhookToken }
    data = json.dumps(data)
    content = requests.post(url, headers=headers, data=data).json()
    return content

def sendMessage(text, webhook):
    if webhook['data']['personEmail'] != bot_email:
    contents = sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "markdown": text,"text": "cos"})
    contents = ''
    return contents
'''
    
    
    