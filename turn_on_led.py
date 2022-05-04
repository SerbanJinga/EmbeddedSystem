# import the needed libraries for turning on a simple led
import RPi.GPIO as GPIO
# for the sleep method --> delays in the program
import time
GPIO.setmode(GPIO.BCM)
# we do not need warnings for this particular program
GPIO.setwarnings(False)
# we setup the 18-th pin for the led
GPIO.setup(18,GPIO.OUT)
# simple print statement
print ("LED on")
# we want to make the led light higher
GPIO.output(18,GPIO.HIGH)
# delay for 1 second
time.sleep(1)
# simple print statement
print("LED off")
# we want to make the led light lower
GPIO.output(18,GPIO.LOW)