import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

try:
    while 1:
        GPIO.output(8, GPIO.HIGH)
        sleep(0.25)
        print "blinker on"
        GPIO.output(8, GPIO.LOW)
        sleep(0.25)
        print "blinker off"
except KeyboardInterrupt:
        GPIO.cleanup()
    

