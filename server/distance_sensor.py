import RPi.GPIO as GPIO
import time
#We're using the physical board pin numbers
GPIO.setmode(GPIO.BOARD)
TRIG = 40
ECHO = 38
GPIO.setup(TRIG,GPIO.OUT) #trigger pin
GPIO.setup(ECHO,GPIO.IN) #echo pin
n = 10# number of iterations for distancemeasurements

def distance():
    dis=0
    for i in range (0,n):
        GPIO.output(TRIG, False) #Waiting For Sensor To Settle"
        time.sleep(0.01) 
        GPIO.output(TRIG, True) #sending pulse
        time.sleep(0.00005) 
        GPIO.output(TRIG, False)
        #Measuring start of the pulse
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        #Measuring end of the pulse
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        dis = dis + (pulse_duration * 17150)/2
    dis=dis/n
    return dis

    