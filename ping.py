#!/usr/bin/env python2.7
"""
Ping Class v0.0
by Yaro Kifor

"""

import time
import RPi.GPIO as GPIO

class Ping:
    triggerPin=0
    echoPin=0
    def __init__(self, triggerPin, echoPin, pinMode=GPIO.BCM):
        self.triggerPin=triggerPin
        self.echoPin=echoPin
        GPIO.setmode(pinMode)
        GPIO.setup(self.triggerPin, GPIO.IN)
        GPIO.output(self.triggerPin, GPIO.LOW)
        GPIO.setup(self.echoPin, GPIO.OUT)
    
    def distance(self):
        GPIO.output(self.triggerPin, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.triggerPin, GPIO.LOW)
        while(GPIO.input(self.echoPin)==0):
            a=0
        timeLength=time.time()
        while(GPIO.input(self.echoPin)==1):
            a=1
        timeLength=time.time()-timeLength
        return timeLength / 170
