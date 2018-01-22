#!/bin/bash

sudo /etc/init.d/ntp stop
sudo ntpd -gq
sudo /etc/init.d/ntp start
