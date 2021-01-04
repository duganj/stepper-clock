"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
#import adafruit_motorkit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())

for i in range(1440):
    kit.stepper1.onestep()
    time.sleep(0.005)
kit.stepper1.release()
