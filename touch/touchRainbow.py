# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio
from ledPixelsPico import *

touch_pad = board.GP18  # Will not work for Circuit Playground Express!
# touch_pad = board.A1  # For Circuit Playground Express

ledPix = ledPixels(12, board.GP0)




ledPix.clear()
                    
print("hello")      
                    
touch = touchio.TouchIn(touch_pad)

n = 0

while True:
    if touch.value:
        ledPix.rainbow(speed=0.005)
    else:
        ledPix.clear()



