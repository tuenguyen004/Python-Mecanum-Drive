#!/usr/bin/env python3
# main.py
#
# The main program of a Mecanum Drive using Adafruit NEMA17 stepper motors 
# driven with Raspberry Pi Model 4B and L298N motor controllers
# 
# The Main Control Loop connects to the robot's drivetrain via SSH into the 
# Raspberry Pi. It initializes the drivetrain to have the wheels locked in place,
# continuously stepping with the current assigned movement. The ReadUserInput 
# program is set up to run in parallel checking for keyboard input to change 
# the movement of the drivetrain. Once a key input is pressed, the ReadUserInput
# received in the equivalent character and checks for any associated movements
# as defined in the MecanumDrive.py module.
#
# Note: Keyboard inputs are detected by isPressed state, not continous inputs
#
# The Default Control Scheme is as followed:
#       SPACEBAR    = stop all movement 
#       "w"         = go forward 
#       "s"         = go backward 
#       "a"         = strafe left 
#       "d"         = strafe right
#       "q"         = rotate left (CCW) 
#       "e"         = rotate right (CW) 
#       "o"         = decrease speed
#       "p"         = increase speed
#       "x"         = reset speed to default
#       "z"         = disconnect from robot
#
# Created by Tue Nguyen (tnguye27)
# December 25th, 2021

import os, pigpio, time
from kbhit import KBHit
from MecanumDrive import MecanumDrive
from threading import Thread


# ================================
# Setting up RaspberryPi GPIO pins
# ================================
os.system("python3 pigpio_setup.py")  
pi = pigpio.pi()
drivetrain = MecanumDrive(pi)
verbose = True  # Prints current program status to stdout


# ===========================================================
# Setting up ReadUserInput Program and Begin Parallel Running
# ===========================================================
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
                # if verbose: print(user_input)
                if user_input == 'z':
                    pass
                
                elif user_input == ' ': 
                    if verbose: print('Stop moving\n')
                    drivetrain.stopMoving()

                elif user_input == 'w':
                    if verbose: print('Going forward\n') 
                    drivetrain.moveForward()

                elif user_input == 's':
                    if verbose: print('Going backward\n') 
                    drivetrain.moveBackward()

                elif user_input == 'a':
                    if verbose: print('Strafing Left\n')
                    drivetrain.moveSidewaysLeft()

                elif user_input == 'd':
                    if verbose: print('Strafing Right\n') 
                    drivetrain.moveSidewaysRight()

                elif user_input == 'q':
                    if verbose: print('Rotating in-place CCW\n') 
                    drivetrain.rotateLeft()

                elif user_input == 'e':
                    if verbose: print('Rotating in-place CW\n') 
                    drivetrain.rotateRight()

                elif user_input == 'o':
                    drivetrain.decreaseSpeed()
                    if verbose: print('Decreasing speed\n') 
                    
                elif user_input == 'p':
                    drivetrain.increaseSpeed()
                    if verbose: print('Increasing speed\n') 
                    
                elif user_input == 'x':
                    drivetrain.resetSpeed()
                    if verbose: print("Reseting back to default speed...\n")
                    
                else:
                    if verbose: print('Input not mapped...\n')
            # else:
                # user_input = "_"
                # drivetrain.stopMoving()
                # print("No keys being pressed\n")
            time.sleep(0.001)
input = ReadUserInput()
inputThread = Thread(target=input.run) 
inputThread.start()


# ==================
# Main Control Loop
# ==================
if verbose: print('\n\n\nConnecting to Robot Chassis...\n')
connectRobot = True                                 # Exit flag
while connectRobot == True:
    # time.sleep(0.01) 
    # # print(user_input)
    drivetrain.run()
    if(user_input == 'z'): connectRobot = False     # Exit Program
    

# ========================
# Clearning Up the Program
# ========================
if verbose: print('Disconnecting to Robot Chassis...\n')
pi.stop()
input.terminate()
os.system("sudo killall pigpiod")  
