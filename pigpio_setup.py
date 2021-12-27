#!/usr/bin/env python3
# pigpio_setup.py
# 
# Automated the setup for pigpio module used in main.py
#
# Credits to user uhoh on Raspberry Pi Stack Exchange (link below)
# https://raspberrypi.stackexchange.com/questions/80271/why-would-os-systemsudo-pigpiod-fail-silently-but-only-part-of-the-time

import time, pigpio, subprocess, logging 

# see if it is running already
status, process = subprocess.getstatusoutput('sudo pidof pigpiod')

if status:  #  it wasn't running, so start it
    print("pigpiod was not running")
    subprocess.getstatusoutput('sudo pigpiod')  # try to  start it
    time.sleep(0.5)
    # check it again        
    status, process = subprocess.getstatusoutput('sudo pidof pigpiod')

if not status:  # if it was started successfully (or was already running)...
    pigpiod_process = process
    print("pigpiod is running, process ID is {} ".format(pigpiod_process))
    try:
        pi = pigpio.pi()  # local GPIO only
        logging.info("pigpio's pi instantiated")
    except Exception as e:
        start_pigpiod_exception = str(e)
        print("problem instantiating pi: {}".format(start_pigpiod_exception))
else:
    print("start pigpiod was unsuccessful.")
