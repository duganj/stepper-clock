"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
import RPi.GPIO as GPIO
#import adafruit_motorkit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

ir = 4

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(ir, GPIO.IN)
kit = MotorKit(i2c=board.I2C())

# if sensor is high, step off of it

if GPIO.input(ir) == 1:
    for i in range(144):
        kit.stepper1.onestep(style = stepper.DOUBLE)
        time.sleep(0.005)

# find home

position = 0

while GPIO.input(ir) == 0:
    print(position)
    position += 1
    kit.stepper1.onestep(style = stepper.DOUBLE)
    time.sleep(0.005)

print("found home!")

position = 0

time.sleep(10)

# step to noon

for i in range(720):
    kit.stepper1.onestep(style = stepper.DOUBLE)
    time.sleep(0.005)

kit.stepper1.release()
GPIO.cleanup()
