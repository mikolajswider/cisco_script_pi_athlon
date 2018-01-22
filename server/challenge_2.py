#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import distance_sensor
import motor
import leds
import video_dir
import car_dir
import spark
import subprocess # To be able to use the function subprocess.call

busnum=1

video_dir.setup(busnum=busnum)
car_dir.setup(busnum=busnum)
motor.setup(busnum=busnum)    
video_dir.home_x_y()
car_dir.home()


def main():
    return none


def start():
    
    motor.stop()
    spark.start()
    video_dir.home_x_y()
    leds.green_led_on()
    time_forward=0
    time_parallel=0 #time spend going towards the parallel wall
    time_check=0.5
    time_turn_left=1.35 #time spent ona turn
    time_turn_right=1.41
    time_turn=2
    #==================================================================================
    # Going straight to wall
    #==================================================================================
    car_dir.home()
    distance_forward = distance_sensor.distance()
    t_f_b=time.time()
    motor.forwardWithSpeed(spd = 100)
    while distance_forward > 50:
        #motor.forward()
        distance_forward = distance_sensor.distance()
    motor.stop()
    t_f_e=time.time()
    time_forward=t_f_e-t_f_b
    
    #==================================================================================
    # Checking where to turn
    #==================================================================================
    video_dir.x_90_l() #turn camera left
    time.sleep(time_check)
    distance_l=distance_sensor.distance()
    video_dir.x_90_r() #turn camera right
    time.sleep(time_check)
    distance_r=distance_sensor.distance()
    video_dir.home_x_y() #set the camera to default again
    
    
    #==================================================================================
    # Turning towards parallel wall
    #==================================================================================
    car_dir.home()
    if distance_l < distance_r:
        car_dir.turn_left()
        motor.forwardWithSpeed(spd = 100)
        time.sleep(time_turn_left)
    else:
        car_dir.turn_right()
        motor.forwardWithSpeed(spd = 100)
        time.sleep(time_turn_right)
    motor.stop()
    car_dir.home()
    
    #==================================================================================
    # taking the first picture after turning
    #==================================================================================
    subprocess.call('/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/take_a_picture.sh') # take_a_pictures uses the webcam connected to the robot to take a picture and store it
    
    #==================================================================================
    # Going straight to parallel wall
    #==================================================================================
    car_dir.home()
    distance_forward = distance_sensor.distance()
    t_t_b=time.time()
    motor.forwardWithSpeed(spd = 100)
    while distance_forward > 15:
        #motor.forward()
        distance_forward = distance_sensor.distance()
    motor.stop()
    # end time on the turn
    t_t_e=time.time()
    time_parallel=t_t_e-t_t_b
    subprocess.call('/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/take_a_picture.sh') # take_a_pictures uses the webcam connected to the robot to take a picture and store it
    text="Distance to wall = "+str(distance_forward)+" cm."
    spark.message(text)
    spark.finish()
    
    #==================================================================================
    # Going back in straight line backward
    #==================================================================================
    car_dir.home()
    motor.backwardWithSpeed(spd = 100)
    time.sleep(time_parallel + time_turn)
    #==================================================================================
    # Turning to finish line
    #==================================================================================
    car_dir.home()
    motor.stop()
    if distance_l < distance_r:
        car_dir.turn_left()
        motor.forwardWithSpeed(spd = 100) 
        time.sleep(time_turn_left)
    else:
        car_dir.turn_right()
        t2=time.time()
        motor.forwardWithSpeed(spd = 100)
        time.sleep(time_turn_right)
    motor.stop()
    
    #==================================================================================
    # Going straight to finish line
    #==================================================================================
    car_dir.home()
    motor.forwardWithSpeed(spd = 100)
    time.sleep(time_forward)
    motor.stop()
    
    leds.green_led_off()

if __name__ == '__main__':
    start()