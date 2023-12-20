'''
REQUIRES:
    * motorU.py
	* ../lib/asyncio
	* ../lib/adafruit_ticks.mpy
'''

from motorU import *
windowMotor = motorU(in1=board.GP9, in2=board.GP10, in3=board.GP11, in4=board.GP12)
for i in range (4):
	windowMotor.rotate(direction = "clockwise")
windowMotor.cleanup()