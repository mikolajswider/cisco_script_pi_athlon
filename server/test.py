#!/usr/bin/env python

import json
import os
import subprocess
import time
import ngrok2
import spark
import leds
import distance_sensor

def main():
    print(distance_sensor.distance())
    
 
if __name__ == "__main__":
    main()