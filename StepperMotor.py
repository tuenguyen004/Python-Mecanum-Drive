#!/usr/bin/env python3
# StepperMotor.py
#
# A Python class implementation of class StepperMotor, specifically designed 
# for driving four-wire bipolar stepper motors (200 steps/rev, 12V, 350mA) 
#
# Created by Tue Nguyen (tnguye27)
# December 25th, 2021

import pigpio
from time import sleep
from collections import deque

halfStepSequence = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]

fullStepSequence = [
    [1, 0, 1, 0], [0, 0, 1, 0],
    [0, 1, 1, 0], [0, 1, 0, 0],
    [0, 1, 0, 1], [0, 0, 0, 1],
    [1, 0, 0, 1], [1, 0, 0, 0]
]

class StepperMotor:
    def __init__(self, pi, pin1, pin2, pin3, pin4, direction=0, sequence=fullStepSequence):
        if not isinstance(pi, pigpio.pi):
            raise TypeError("Is not pigpio.pi instance.")
        self.pi = pi
        pi.set_mode(pin1, pigpio.OUTPUT)
        pi.set_mode(pin2, pigpio.OUTPUT)
        pi.set_mode(pin3, pigpio.OUTPUT)
        pi.set_mode(pin4, pigpio.OUTPUT)
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.direction = direction
        self.deque = deque(sequence)

    def setDirection(self, direction):
        self.direction = direction  
                                    
    def doStepAndDelay(self, delayAfterStep):
        if(self.direction == 1):        # 1 = clockwise 
            self.deque.rotate(-1)
        elif(self.direction == -1):     # -1 = counterclockwise
            self.deque.rotate(1)
        else:
            return
        step = self.deque[0]
        self.pi.write(self.pin1, step[0])
        self.pi.write(self.pin2, step[1])
        self.pi.write(self.pin3, step[2])
        self.pi.write(self.pin4, step[3])
        sleep(delayAfterStep)
