'''
REQUIRES:
    * ledPixelsPico.py
    * neopixel.mpy
'''

import board
from ledPixelsPico import *

ledPix = ledPixels(20, board.GP22)

#ledPix.light(4, (0, 100, 0))
ledPix.brightness = 0.1
ledPix.rainbow(speed=0.005)
print("hi")