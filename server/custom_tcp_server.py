#!/usr/bin/env python

# =============================================================================
# Custom file, based on tcp_server.by, used for pi-athlon challenges
# =============================================================================

import RPi.GPIO as GPIO
import spark # File created for spark communication, contains start, list and finish functions [by Miko]
import challenge_2 # File created for second challenge, contains fuctions necessary for the challenge to be successfull [by Miko]
import subprocess # To be able to use the function subprocess.call
import video_dir
import car_dir
import motor
import leds
from socket import *
from time import ctime          # Import necessary modules   
import time
import test

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home', 'x_90_l','x_90_r','ntp','ntp_cisco','pic','spark_start','spark_finish','challenge_2']

busnum = 1          # Edit busnum to 0, if you uses Raspberry Pi 1 or 0

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     # The parameter of listen() defines the number of connections permitted at one time. Once the 
                         # connections are full, others will be rejected. 

video_dir.setup(busnum=busnum)
car_dir.setup(busnum=busnum)
motor.setup(busnum=busnum)     # Initialize the Raspberry Pi GPIO connected to the DC motor. 
video_dir.home_x_y()
car_dir.home()
motor.stop() #stop the motors in case of previous ungracefull shutdown
leds.green_led_off() #turns the led of in case of previous ungracefull shutdown

while True:
	print 'Waiting for connection...'
	# Waiting for connection. Once receiving a connection, the function accept() returns a separate 
	# client socket for the subsequent communication. By default, the function accept() is a blocking 
	# one, which means it is suspended before the connection comes.
	tcpCliSock, addr = tcpSerSock.accept() 
	print '...connected from :', addr     # Print the IP address of the client connected with the server.

	while True:
		data = ''
		data = tcpCliSock.recv(BUFSIZ)    # Receive data sent from the client. 
		# Analyze the command received and control the car accordingly.
		if not data:
			break
		if data == ctrl_cmd[0]:
			print 'motor moving forward'
			motor.forward()
		elif data == ctrl_cmd[1]:
			print 'recv backward cmd'
			motor.backward()
		elif data == ctrl_cmd[2]:
			print 'recv left cmd'
			car_dir.turn_left()
		elif data == ctrl_cmd[3]:
			print 'recv right cmd'
			car_dir.turn_right()
		elif data == ctrl_cmd[6]:
			print 'recv home cmd'
			car_dir.home()
		elif data == ctrl_cmd[4]:
			print 'recv stop cmd'
			motor.ctrl(0)
		elif data == ctrl_cmd[5]:
			print 'read cpu temp...'
			temp = cpu_temp.read()
			tcpCliSock.send('[%s] %0.2f' % (ctime(), temp))
		elif data == ctrl_cmd[8]:
			print 'recv x+ cmd'
			video_dir.move_increase_x()
		elif data == ctrl_cmd[9]:
			print 'recv x- cmd'
			video_dir.move_decrease_x()
		elif data == ctrl_cmd[10]:
			print 'recv y+ cmd'
			video_dir.move_increase_y()
		elif data == ctrl_cmd[11]:
			print 'recv y- cmd'
			video_dir.move_decrease_y()
		elif data == ctrl_cmd[12]:
			print 'home_x_y'
			#test.test()
			video_dir.home_x_y()
		elif data == ctrl_cmd[13]:
			print 'x_90_l'
			video_dir.x_90_l()	
		elif data == ctrl_cmd[14]:
			print 'x_90_r'
			video_dir.x_90_r()
		elif data == ctrl_cmd[15]:
			print 'ntp'
			subprocess.call('/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/set_ntp.sh') # set_ntp.sh sets the ntp when outside of blizzard network
		elif data == ctrl_cmd[16]:
			print 'ntp_cisco'
			subprocess.call('/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/set_ntp_cisco.sh') # set_ntp_cisco sets the ntp when inside of blizzard network
		elif data == ctrl_cmd[17]:
			print 'pic'
			subprocess.call('/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/take_a_picture.sh') # take_a_pictures uses the webcam connected to the robot to take a picture and store it
		elif data == ctrl_cmd[18]:
			print 'spark_start'
                        spark.start()
		elif data == ctrl_cmd[19]:
			print 'spark_finish'
    			spark.finish()
                elif data == ctrl_cmd[20]:
			print 'challenge_2'
			challenge_2.start()
		elif data[0:5] == 'speed':     # Change the speed
			print data
			numLen = len(data) - len('speed')
			if numLen == 1 or numLen == 2 or numLen == 3:
				tmp = data[-numLen:]
				print 'tmp(str) = %s' % tmp
				spd = int(tmp)
				print 'spd(int) = %d' % spd
				if spd < 24:
					spd = 24
				motor.setSpeed(spd)
		elif data[0:5] == 'turn=':	#Turning Angle
			print 'data =', data
			angle = data.split('=')[1]
			try:
				angle = int(angle)
				car_dir.turn(angle)
			except:
				print 'Error: angle =', angle
		elif data[0:8] == 'forward=':
			print 'data =', data
			spd = data[8:]
			try:
				spd = int(spd)
				motor.forward(spd)
			except:
				print 'Error speed =', spd
                elif data[0:9] == 'backward=':
                        print 'data =', data
                        spd = data.split('=')[1]
			try:
				spd = int(spd)
	                        motor.backward(spd)
			except:
				print 'ERROR, speed =', spd

		else:
			print 'Command Error! Cannot recognize command: ' + data

tcpSerSock.close()