"""Simple test for using adafruit_motorkit with a stepper motor"""
import sys
import time
import board
import ntplib
from datetime import datetime, timezone
import pytz
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import RPi.GPIO as GPIO

# ir sensor on GPIO pin 4
ir = 4
GPIO.setup(ir, GPIO.IN)

clock = MotorKit(i2c=board.I2C())

c = ntplib.NTPClient()

# if sensor is high, step off of it

if GPIO.input(ir) == 1:
    for i in range(144):
        clock.stepper1.onestep(style = stepper.DOUBLE)
        time.sleep(0.005)

# find home

position = 0

while GPIO.input(ir) == 0:
    print(position)
    position += 1
    clock.stepper1.onestep(style = stepper.DOUBLE)
    time.sleep(0.005)
    if position > 1500:
        print("can't find home, quitting")
        clock.stepper1.release()
        sys.exit()

print("found home!")

position = 0

# now get the current time
# Provide the respective ntp server ip in below function
response = c.request('time.nist.gov', version=3)
response.offset

utctime = datetime.fromtimestamp(response.tx_time, timezone.utc)
print(utctime)

localtime = utctime.astimezone(pytz.timezone('America/Los_Angeles'))
print(localtime)

# calculate current time position
hours = time.strftime('%H')
mins = time.strftime('%M')
ihours = int(hours)
imins = int(mins)
position = ihours*60 + imins
print("current time position:", position)

# step to current time position

for i in range(position):
    clock.stepper1.onestep(style = stepper.DOUBLE)
    time.sleep(0.005)

print("clock is set")
clock.stepper1.release()
GPIO.cleanup()
