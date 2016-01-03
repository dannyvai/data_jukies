#rc.local : screen -dm -t "punch"  bash -c "python /home/pi/button_click.py;sleep 10000"

import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 12)  
import time
import os
import datetime
import httplib

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN)    # set GPIO25 as input (button)  
GPIO.setup(24, GPIO.OUT)

#Just so we know if it is up yet
GPIO.output(24, 1)
time.sleep(0.5)
GPIO.output(24, 0)

last_state = False
try:
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(25) and not last_state : # if port 25 == 1  
            #click_time =  time.strftime("%H:%M:%S")
            last_state = True
            os.system('date >> data.txt')
            print "We got a click"
            conn = httplib.HTTPConnection("www.yourdomain.com",8000)
            conn.request("GET","/punchin")
            print res.status, res.reason
            data = res.read()
            print len(data)
            GPIO.output(24, 1)
        elif not GPIO.input(25) and last_state:
            #print "Port 25 is 0/LOW/False - LED OFF"  
            last_state = False
            GPIO.output(24, 0)
        sleep(0.1)         # wait 0.1 seconds  

finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself 



