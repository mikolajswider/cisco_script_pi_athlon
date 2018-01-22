#! /usr/bin/python
import datetime
import requests
import time
import os #use linux commands
import spark


# =====================================================================================================
# old_ip reads from /home/pi/Destkop/scripts/general/ip the old ip address assigned to wlan 0 interface
# =====================================================================================================

def old_ip():
    l=[]
    with open ("/home/pi/pi-athlon/server/ip.txt", 'r') as f:
        for line in f:
            l.append(line.rstrip('\n'))
    f.close()
    return l

# =====================================================================================================
# new_ip reads the current ip address assigned to wlan 0 interface 'ifconfig wlan | grep "inet addr"'
# =====================================================================================================

def new_ip():
    l=[]
    l.append(os.popen('/sbin/ifconfig wlan | grep "inet addr"').read().rstrip('\n'))
    #ifconfig= output = os.popen('ifconfig wlan | grep "inet addr"').read()
    return l

# =====================================================================================================
# main checks if the old and new ip addresses are different, if different,
# saves the new ip to home/pi/Destkop/scripts/general/ip and publish it to the spark room mgs3X
# =====================================================================================================


def main():
    room_id = spark.mgs3x_room_id()
    token = spark.mgs3x_token()
    oldip=old_ip()
    newip=new_ip()
    
    if oldip!=newip:
        spark.message(room_id, token, newip[0])
        with open ("/home/pi/pi-athlon/server/ip.txt", 'w') as f:
            f.write(newip[0])
        f.close()
        
    #print(response.status_code)
    # response_json = response.json()
    #print(response.text)
    # print(response_json['roomId'])
    # print(response.json)
    

if __name__ == '__main__':
    main()