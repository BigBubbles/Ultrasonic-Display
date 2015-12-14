#!/usr/bin/env python2.7
"""
 Ping Class v0.0
 by Yaro Kifor

 Used sunfounder as a reference
 http://www.sunfounder.com/index.php?c=case_incs&a=detail_&id=309&name=Sensor%20Kit%20for%20B+

 """

import time
import RPi.GPIO as GPIO

#Exception for if a callback is called
class CallbackCalled(Exception):
    pass
        
class Ping:
    triggerPin=0
    echoPin=0
    def __init__(self, triggerPin, echoPin, pinMode=GPIO.BCM):
        #Set private varibles
        self.triggerPin=triggerPin
        self.echoPin=echoPin
        #Setup pin and set out put pins to low
        GPIO.setmode(pinMode)
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.output(self.triggerPin, GPIO.LOW)
        GPIO.setup(self.echoPin, GPIO.IN)

    def _triggerSensor(self):
        GPIO.output(self.triggerPin, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(self.triggerPin, GPIO.LOW)
        
    def _echoFalling(self,a):
        #Raise CallbackCalled to be catched
        raise Callbackcalled()
    
    #Needs testing
    def distance(self, timeout=0):
        #If timeout is 0 then timeout is forever
        if timeout == 0:
            #self._triggerSensor()
            #GPIO.output(self.triggerPin, GPIO.HIGH)
            #time.sleep(0.00001)
            #GPIO.output(self.triggerPin,GPIO.LOW)
            #Wait for raising edge
            #GPIO.wait_for_edge(self.echoPin,GPIO.RISING)
            while(GPIO.input(self.echoPin)==0):
                a=0
            #Get epoch time
            echoLength=time.time()
            #Wait for falling edge 
            #GPIO.wait_for_edge(self.echoPin,GPIO.FALLING)
            while(GPIO.input(self.echoPin)==1):
                a=0
            #Get how long the echoPin was high for
            echoLength=time.time()-echoLength
            print("DONE.")
            #Return in meters what sensor deteced
            # length of echo * 343.2 (speed of sound in m/s) / 2 (half the distance) * 100 (for cm)
            return echoLength * 171600
        else:
            echoLength=0
            try:            
                #Add the event for the call back
                GPIO.add_event_detect(self.echoPin,GPIO.FALLING,callback=self._echoFalling)
                self._triggerSensor()
                #Get epoch time
                while(GPIO.input(self.echoPin)==1):
                    a=1
                echoLength=time.time()
                #Wait for the timeout
                time.sleep(timeout)
                #Remove event callback
                GPIO.remove_event_callback(self.echoPin)
                #Return -1 as failure
                return -1
            except CallbackCalled:
                #Sets echoLength to how echoPin was high
                echoLength=echoLength-time.time()
                #Remove event callback it doesn't need to be called again
                GPIO.remove_event_callback(self.echoPin)
                return echoLength * 171600
