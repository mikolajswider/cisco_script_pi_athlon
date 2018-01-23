#!/usr/bin/env python
import wsgiref.handlers
import subprocess
import json
import requests
import datetime
import requests
import time
import os #use linux commands
from requests_toolbelt.multipart.encoder import MultipartEncoder

webhookID = "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svZTU4NGRhZDQtZmRhMC00ODc1LTk0ZWItNDljZTU2MjRjNjRi"
webhookToken = "NjdlZjE2MjQtZTQ0NS00OTcyLWJhNDMtNTc5NzkyNTk3ZGRkYTk1M2VjMWYtZjFi"
HELLO_WORLD = "czesc"
bot_email = "3Dprinter@sparkbot.io"
roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vZGY0Y2M3NjAtNTJhMi0xMWU3LThhY2UtYWI1MjZhNjgxNDE3"

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

def makePhoto(webhook):
    #path_file = "/home/pi/Desktop/scripts/cam.jpg"
    path_file = "/home/pi/cam.jpg"
    url = "https://api.ciscospark.com/v1/messages"
    multipart_data = MultipartEncoder(
    fields={
    # a file upload field
    'files': ("name", open(path_file, 'rb'), 'image/jpg'),
    # plain text fields
    #'text': 'Picture',
    'roomId': webhook['data']['roomId'],
    })
    header={'Authorization': 'Bearer ' + webhookToken, 'Content-Type': multipart_data.content_type} # define the header which will allow mgs3X-Robot to communicate with Spark
    #body={"roomId": test_room_Id, "text": "Pi-Athlon Robot Metal Gear 3X - finish time: " +time.strftime("%H:%M:%S")+" CET, "+time.strftime("%d/%m/%Y")
    contents = requests.post(url, headers=header, data=multipart_data)
    return contents

def application(environ, start_response):
    status = '200 OK'
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    if request_body_size > 0:
        webhook = environ['wsgi.input'].read(request_body_size)
        webhook = json.loads(webhook)
        result = sendSparkGET('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))
        if webhook['data']['personEmail'] != bot_email:
            if result['text'] == "3Dprinter show picture" or result['text'] == "3Dprinter show photo"  or result['text'] == "show photo" or result['text'] == "show picture":
                subprocess.call("/home/pi/Desktop/scripts/make_a_photo.sh")
                makePhoto(webhook)
            elif result['text'] == "3Dprinter show misliwin" or result['text'] == "show misliwin" or result['text'] == "Show misliwin" or result['text'] == "3Dprinter Show misliwin":
                content = sendMessage("Milosz Sliwinski (misliwin) and Mikolaj Swider (mswider) are the initiators and contributors of the 'Monitoring 3D Printing Status' project at Cisco Krakow. Do not hesitate to ping them if you have questions or improvement propositions regarding the project.", webhook)
            elif result['text'] == "3Dprinter show mswider" or result['text'] == "show mswider" or result['text'] == "3Dprinter Show mswider" or result['text'] == "Show mswider":
                content = sendMessage("Mikolaj Swider (mswider) and Milosz Sliwinski (misliwin) are the initiators and contributors of the 'Monitoring 3D Printing Status' project at Cisco Krakow. Do not hesitate to ping them if you have questions or improvement propositions regarding the project.", webhook)
            elif result['text'] == "3Dprinter show commands" or result['text'] == "show commands":
                content = sendMessage("Here is the list of valid commands: show commands, show misliwin, show mswider, show photo, show picture, show status, show special-thanks. Please note that you can use a capital letter at the beginning of each command. For instance both 'show picture' and 'Show picture will be accepted.", webhook)
            elif result['text'] == "3Dprinter show special-thanks" or result['text'] == "show special-thanks":
                content = sendMessage("Special thanks to Dorota Bek (dbek) who encouraged us to work on the project and provided us with the raspi camera, to Pawel Molicki (pmolicki) who provided us with the raspberry pi and chager and Bartosz Nowak (banowak) who allowed us to buy and expense the PLA material.", webhook)
            elif result['text'] == "3Dprinter show ip" or result['text'] == "show ip" or result['text'] == "3Dprinter Show ip" or result['text'] == "Show ip":
                ip = os.popen('/sbin/ifconfig wlan0 | /bin/grep "inet "').read()
                content = sendMessage(ip, webhook)
            elif result['text'] == "3Dprinter show status" or result['text'] == "3Dprinter Show status" or result['text'] == "show status" or result['text'] == "Show status":
                content = sendMessage("Command in developement. Please be patient.", webhook)
            elif result['text'] == "3Dprinter show hostname" or result['text'] == "3Dprinter Show hostname" or result['text'] == "show hostname" or result['text'] == "Show hostname":
                content = sendMessage("3D_printer_pi", webhook)
            elif result['text'] == "3Dprinter " or result['text'] == "3Dprinter Show hostname" or result['text'] == "show hostname" or result['text'] == "Show hostname":
                content = sendMessage("3D_printer_pi", webhook)
            else:
                content = sendMessage("Invalid command. Here is the list of valid commands: show commands, show misliwin, show mswider, show photo, show picture, show ip, show status, show special-thanks. Please note that you can use a capital letter at the beginning of each command. For instance both 'show picture' and 'Show picture' commands will be accepted.", webhook)
    else:
        content = HELLO_WORLD
        response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
        start_response(status, response_headers)
        yield content.encode('utf8')
    
if __name__ == '__main__':
    wsgiref.handlers.CGIHandler().run(application)