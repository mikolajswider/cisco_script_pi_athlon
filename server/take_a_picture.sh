#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")

fswebcam -r 800x600 --no-banner /home/pi/Pictures/pi_athlon/pic_$DATE.jpg

