#!/usr/bin/env python3
# MecanumDrive.py
#
# A Python class implementation of Mecanum Drive and its associated motion
#
# Created by Tue Nguyen (tnguye27)
# December 25th, 2021

from StepperMotor import StepperMotor

class MecanumDrive:
    def __init__(self, pi, maxSpeed=0.0025, modifier=0.5):
        self.FrontLeft = StepperMotor(pi, 4, 17, 27, 22)
        self.FrontRight = StepperMotor(pi, 18, 23, 24, 25)
        self.BackLeft = StepperMotor(pi, 6, 13, 19, 26)
        self.BackRight = StepperMotor(pi, 12, 16, 20, 21)
        self.speed = maxSpeed * modifier
    
    def run(self):
        self.FrontLeft.doStepAndDelay(self.speed)
        self.FrontRight.doStepAndDelay(self.speed)
        self.BackLeft.doStepAndDelay(self.speed)
        self.BackRight.doStepAndDelay(self.speed)

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
    