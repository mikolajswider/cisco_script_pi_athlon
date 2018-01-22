#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
# Custom file, based on client_App.by, used for pi-athlon challenges
# ============================================================================= 

import subprocess
import time
from Tkinter import *
from socket import *      # Import necessary module

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home', 'x_90_l','x_90_r','ntp','ntp_cisco','pic','spark_start','spark_finish','challenge_2']

top = Tk()   # Create a top window
top.title('Sunfounder Raspberry Pi Smart Video Car')

HOST = '127.0.0.1'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

# =============================================================================
# The function is to send the command forward to the server, so as to make the 
# car move forward.
# ============================================================================= 
def forward_fun(event):
	print 'forward'
	tcpCliSock.send('forward')

def backward_fun(event):
	print 'backward'
	tcpCliSock.send('backward')

def left_fun(event):
	print 'left'
	tcpCliSock.send('left')

def right_fun(event):
	print 'right'
	tcpCliSock.send('right')

def stop_fun(event):
	print 'stop'
	tcpCliSock.send('stop')

def home_fun(event):
	print 'home'
	tcpCliSock.send('home')

def x_increase(event):
	print 'x+'
	tcpCliSock.send('x+')

def x_decrease(event):
	print 'x-'
	tcpCliSock.send('x-')

def y_increase(event):
	print 'y+'
	tcpCliSock.send('y+')

def y_decrease(event):
	print 'y-'
	tcpCliSock.send('y-')

def xy_home(event):
	print 'xy_home'
	tcpCliSock.send('xy_home')
	
# =============================================================================
# Newly defined functions for Challenge 1 of pi-athlon
# ============================================================================= 

def x_90_l(event):
	print 'x_90_l'
	tcpCliSock.send('x_90_l')

def ntp(event):
	print 'ntp'
	tcpCliSock.send('ntp')

def ntp_cisco(event):
	print 'ntp_cisco'
	tcpCliSock.send('ntp_cisco')
	
def pic(event):
	print 'pic'
	tcpCliSock.send('pic')
	
def spark_start(event):
	print 'spark_start'
	tcpCliSock.send('spark_start')

def spark_finish(event):
	print 'spark_finish'
	tcpCliSock.send('spark_finish')

# =============================================================================
# Newly defined functions for Challenge 2 of pi-athlon
# ============================================================================= 

def challenge_2(event):
	print'challenge_2'
	tcpCliSock.send('challenge_2')

def x_90_r(event):
	print 'x_90_r'
	tcpCliSock.send('x_90_r')

# =============================================================================

def max_speed(event):
    global spd
    spd=100
    print 'sendData = %s' % data
    tcpCliSock.send(data) 

spd =100

def changeSpeed(ev=None):
	tmp = 'speed'
	global spd
	spd = speed.get()
	data = tmp + str(spd)  # Change the integers into strings and combine them with the string 'speed'. 
	print 'sendData = %s' % data
	tcpCliSock.send(data)  # Send the speed data to the server(Raspberry Pi)

label = Label(top, text='Speed:', fg='blue')  # Create a label
label.grid(row=4, column=1)                  # Label layout


speed = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=changeSpeed)  # Create a scale
speed.set(50)
speed.grid(row=5, column=1)

# =============================================================================
# Exit the GUI program and close the network connection between the client 
# and server.
# =============================================================================
def quit_fun(event):
	top.quit()
	tcpCliSock.send('stop')
	tcpCliSock.close()

# =============================================================================
# Create buttons
# =============================================================================
Btn0 = Button(top, width=9, text='Forward (w)', bg='blue')
Btn1 = Button(top, width=9, text='Backward (s)', bg='blue')
Btn2 = Button(top, width=9, text='Left (a)', bg='blue')
Btn3 = Button(top, width=9, text='Right (d)', bg='blue')
Btn4 = Button(top, width=9, text='Quit')
Btn5 = Button(top, width=9, height=2, text='HOME (f)', bg='blue')

# =============================================================================
# Buttons layout
# =============================================================================
Btn0.grid(row=0,column=1)
Btn1.grid(row=2,column=1)
Btn2.grid(row=1,column=0)
Btn3.grid(row=1,column=2)
Btn4.grid(row=7,column=7)
Btn5.grid(row=1,column=1)

# =============================================================================
# Bind the buttons with the corresponding callback function.
# =============================================================================
Btn0.bind('<ButtonPress-1>', forward_fun)  # When button0 is pressed down, call the function forward_fun().
Btn1.bind('<ButtonPress-1>', backward_fun)
Btn2.bind('<ButtonPress-1>', left_fun)
Btn3.bind('<ButtonPress-1>', right_fun)
Btn0.bind('<ButtonRelease-1>', stop_fun)   # When button0 is released, call the function stop_fun().
Btn1.bind('<ButtonRelease-1>', stop_fun)
Btn2.bind('<ButtonRelease-1>', stop_fun)
Btn3.bind('<ButtonRelease-1>', stop_fun)
Btn4.bind('<ButtonRelease-1>', quit_fun)
Btn5.bind('<ButtonRelease-1>', home_fun)

# =============================================================================
# Create buttons
# =============================================================================
Btn07 = Button(top, width=9, text='Cam Right (l)', bg='orange')
Btn08 = Button(top, width=9, text='Cam Left (j)', bg='orange')
Btn10 = Button(top, width=9, text='Cam Up (i)', bg='orange')
Btn09 = Button(top, width=9, text='Cam Down (k)', bg='orange')
Btn11 = Button(top, width=9, height=2, text='HOME (h)', bg='orange')

# =============================================================================
# Buttons layout
# =============================================================================
Btn07.grid(row=1,column=5)
Btn08.grid(row=1,column=3)
Btn09.grid(row=2,column=4)
Btn10.grid(row=0,column=4)
Btn11.grid(row=1,column=4)

# =============================================================================
# Bind button events
# =============================================================================
Btn07.bind('<ButtonPress-1>', x_increase)
Btn08.bind('<ButtonPress-1>', x_decrease)
Btn09.bind('<ButtonPress-1>', y_decrease)
Btn10.bind('<ButtonPress-1>', y_increase)
Btn11.bind('<ButtonPress-1>', xy_home)
#Btn07.bind('<ButtonRelease-1>', home_fun)
#Btn08.bind('<ButtonRelease-1>', home_fun)
#Btn09.bind('<ButtonRelease-1>', home_fun)
#Btn10.bind('<ButtonRelease-1>', home_fun)
#Btn11.bind('<ButtonRelease-1>', home_fun)

# ================================================================================
# Create buttons for taking pictures, sending information to Spark and setting NTP
# ================================================================================
Btn12 = Button(top, width=10, text='Spark Start (9)', bg='green')
Btn13 = Button(top, width=10, text='Picture (q)', bg='yellow')
Btn14 = Button(top, width=10, text='Spark Finish (0)', bg='green')
Btn15 = Button(top, width=10, text='Set NTP', bg='grey')
Btn16 = Button(top, width=10, text='Set NTP (Cisco)', bg='grey')
#Btn17 = Button(top, width=10, text='Laser Off. (r)', bg='red')
Btn18 = Button(top, width=12, text='Camera 90 Left (u)', bg='orange')
Btn19 = Button(top, width=12, text='Camera 90 Right (o)', bg='orange')
Btn20 = Button(top, width=10, text='Challenge 2 ', bg='red')
# =============================================================================
# Buttons layout in a new column
# =============================================================================
Btn12.grid(row=0,column=7)
Btn13.grid(row=1,column=7)
Btn14.grid(row=2,column=7)

label_ntp = Label(top, text='NTP:', fg='grey')  # Create a label
label_ntp.grid(row=6, column=0)                  # Label layout
Btn15.grid(row=7,column=0)
Btn16.grid(row=8,column=0)

#Btn17.grid(row=8,column=0)
Btn18.grid(row=4,column=4)
Btn19.grid(row=5,column=4)
Btn20.grid(row=10,column=10)
# =============================================================================
# Bind the buttons with the corresponding callback function.
# =============================================================================
Btn12.bind('<ButtonRelease-1>', spark_start)
Btn13.bind('<ButtonRelease-1>', pic)
Btn14.bind('<ButtonRelease-1>', spark_finish)
Btn15.bind('<ButtonRelease-1>', ntp)
Btn16.bind('<ButtonRelease-1>', ntp_cisco)
#Btn17.bind('<ButtonRelease-1>', laseroff)
Btn18.bind('<ButtonRelease-1>', x_90_l)
Btn19.bind('<ButtonRelease-1>', x_90_r)
Btn20.bind('<ButtonRelease-1>', challenge_2)
# =============================================================================
# Bind buttons on the keyboard with the corresponding callback function to 
# control the car remotely with the keyboard.
# =============================================================================
top.bind('<KeyPress-a>', left_fun)   # Press down key 'A' on the keyboard and the car will turn left.
top.bind('<KeyPress-d>', right_fun)
top.bind('<KeyPress-s>', backward_fun)
top.bind('<KeyPress-w>', forward_fun)
top.bind('<KeyPress-f>', home_fun)
top.bind('<KeyRelease-a>', home_fun) # Release key 'A' and the car will turn back.
top.bind('<KeyRelease-d>', home_fun)
top.bind('<KeyRelease-s>', stop_fun)
top.bind('<KeyRelease-w>', stop_fun)

#===============================================================================
# Bind buttons on the keyboard with the corresponding callback function to 
# control the camera
#===============================================================================
top.bind('<KeyPress-i>', y_increase)
top.bind('<KeyPress-k>', y_decrease)
top.bind('<KeyPress-l>', x_increase)
top.bind('<KeyPress-j>', x_decrease)
top.bind('<KeyPress-h>', xy_home)
top.bind('<KeyRelease-q>', pic)
top.bind('<KeyRelease-u>', x_90_l)
top.bind('<KeyRelease-o>', x_90_r)
#===============================================================================
# Bind buttons on the keyboard in order the laser
#===============================================================================
#top.bind('<KeyPress-e>', laseron)
#top.bind('<KeyRelease-r>', laseroff)
#===============================================================================
# Bind buttons on the keyboard with the corresponding callback function to 
# send messages to Spark
#===============================================================================
top.bind('<KeyRelease-9>', spark_start)
top.bind('<KeyRelease-0>', spark_finish)

#===============================================================================
# Bind buttons on the keyboard with the corresponding callback function to 
# send messages to Spark
#===============================================================================
#top.bind('<KeyRelease-t>', ntp)

def main():
	top.mainloop()

if __name__ == '__main__':
	main()

