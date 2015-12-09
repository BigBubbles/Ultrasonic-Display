#!/usr/bin/env python2.7
"""
Ping Class v0.0
by Yaro Kifor

 used sunfounder as a reference
 http://www.sunfounder.com/index.php?c=case_incs&a=detail_&id=309&name=Sensor%20Kit%20for%20B+

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
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.output(self.triggerPin, GPIO.LOW)
        GPIO.setup(self.echoPin, GPIO.IN)
    
    def distance(self):
		#Trigger the sensor
        GPIO.output(self.triggerPin, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.triggerPin, GPIO.LOW)
		#Wait for raising edge
        while(GPIO.input(self.echoPin)==0):
            a=0
		#Get epoch time
        timeLength=time.time()
        #Wait for falling edge
		while(GPIO.input(self.echoPin)==1):
            a=1
		#Get how long the echoPin was high for
        timeLength=time.time()-timeLength
		#Return in meters what sensor deteced
		# length of echo * 340 (speed of sound) / 2 (half the distance)
        return timeLength / 170
