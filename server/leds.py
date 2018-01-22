#!/usr/bin/env python
import RPi.GPIO as GPIO
import time    # Import necessary modules

GPIO.setmode(GPIO.BOARD)
#Defines the pin controlling led
pin = 36
#Defines how to use the led pin
GPIO.setup(pin, GPIO.OUT)

def green_led_off():
    #Led is being turned on
    GPIO.output(pin, GPIO.LOW)
    
def green_led_on():
    #Led is being turned on
    GPIO.output(pin, GPIO.HIGH)
