#!/usr/bin/env python3
# threading_test.py
# 
# A simple Python script used to test multithreading on Raspberry Pi
#
# Credits to Rob's Raspberry Pi Blog (link below)
# http://robsraspberrypi.blogspot.com/2016/01/raspberry-pi-python-threading.html

import time
from threading import Thread
from kbhit import KBHit

global user_input
user_input = "_"

class ReadUserInput:
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global user_input
        keyboard = KBHit()
        while self._running:
            if(not self._running):
                break
            if keyboard.kbhit():
                user_input = keyboard.getch()
                print(user_input)
                if user_input == 'z': 
                    print('Disconnecting from Robot...\n')
                elif user_input == 'w':
                    print('Going forward\n') 
                elif user_input == 's':
                    print('Going backward\n') 
                elif user_input == 'a':
                    print('Strafing Left\n')
                elif user_input == 'd':
                    print('Strafing Right\n') 
                elif user_input == 'q':
                    print('Rotating in-place CCW\n') 
                elif user_input == 'e':
                    print('Rotating in-place CW\n') 
                else:
                    print('Input not mapped, staying still...\n')
            else:
                user_input = "_"
                # print("No keys being pressed\n")
            time.sleep(0.01)

# Create an instance, thread the run function, and then start thread
input = ReadUserInput()
inputThread = Thread(target=input.run) 
inputThread.start()


Exit = False 
while Exit==False:
    time.sleep(0.01)
    print("%s" %(user_input))
    if(user_input == 'z'): Exit = True 

input.terminate()
print("Goodbye :)")