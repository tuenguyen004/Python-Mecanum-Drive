#!/usr/bin/env python3
# MecanumDrive.py
#
# A Python class implementation of Mecanum Drive and its associated movements
#
# Created by Tue Nguyen (tnguye27)
# December 25th, 2021
 
from StepperMotor import StepperMotor

steps_per_revolution = 200
speedAdjust = [0.25, 0.5, 1, 1.25, 1.5]     # 0.25 is fastest, 1.5 is slowest

class MecanumDrive:
    def __init__(self, pi, maxSpeed=0.0025, speedLevel=2):
        self.FrontLeft = StepperMotor(pi, 4, 17, 27, 22)
        self.FrontRight = StepperMotor(pi, 18, 23, 24, 25)
        self.BackLeft = StepperMotor(pi, 6, 13, 19, 26)
        self.BackRight = StepperMotor(pi, 12, 16, 20, 21)
        self.maxSpeed = maxSpeed 
        self.speedModifierIndex = speedLevel

    def run(self):
        speed = self.maxSpeed * speedAdjust[self.speedModifierIndex]
        self.FrontLeft.doStepAndDelay(speed)
        self.FrontRight.doStepAndDelay(speed)
        self.BackLeft.doStepAndDelay(speed)
        self.BackRight.doStepAndDelay(speed)

    def moveForward(self):
        self.FrontLeft.setDirection(1)
        self.FrontRight.setDirection(1)
        self.BackLeft.setDirection(1)
        self.BackRight.setDirection(1)

    def moveBackward(self): 
        self.FrontLeft.setDirection(-1)
        self.FrontRight.setDirection(-1)
        self.BackLeft.setDirection(-1)
        self.BackRight.setDirection(-1)

    def moveSidewaysRight(self):
        self.FrontLeft.setDirection(1)
        self.FrontRight.setDirection(-1)
        self.BackLeft.setDirection(-1)
        self.BackRight.setDirection(1)

    def moveSidewaysLeft(self): 
        self.FrontLeft.setDirection(-1)
        self.FrontRight.setDirection(1)
        self.BackLeft.setDirection(1)
        self.BackRight.setDirection(-1)

    def rotateRight(self): 
        self.FrontLeft.setDirection(-1)
        self.FrontRight.setDirection(1)
        self.BackLeft.setDirection(-1)
        self.BackRight.setDirection(1)

    def rotateLeft(self): 
        self.FrontLeft.setDirection(1)
        self.FrontRight.setDirection(-1)
        self.BackLeft.setDirection(1)
        self.BackRight.setDirection(-1)

    def stopMoving(self): 
        self.FrontLeft.setDirection(0)
        self.FrontRight.setDirection(0)
        self.BackLeft.setDirection(0)
        self.BackRight.setDirection(0)

    # Note: Please identify a functional speed (delay time) that the drivetrain 
    # can safely operate on and modify the speedAdjust list above as needed to
    # avoid any hardware damage to the motors and chassis
    def increaseSpeed(self):
        if self.speedModifierIndex == 0:
            print("Can't go any faster than allowed speed!")
        else:
            self.speedModifierIndex -= 1
        print("Current RPM: %d\n" %(60/(self.maxSpeed * 8 * steps_per_revolution * 
                                    speedAdjust[self.speedModifierIndex])))
    
    def decreaseSpeed(self):
        if self.speedModifierIndex == 4:
            print("Can't go any slower than allowed speed!")
        else:
            self.speedModifierIndex += 1
        print("Current RPM: %d\n" %(60/(self.maxSpeed * 8 * steps_per_revolution * 
                                    speedAdjust[self.speedModifierIndex])))

    def resetSpeed(self):
        self.speedModifierIndex = 1
        print("Current RPM: %d\n" %(60/(self.maxSpeed * 8 * steps_per_revolution * 
                                      speedAdjust[self.speedModifierIndex])))