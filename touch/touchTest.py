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

n = -1

while True:
    
    n += 1
    print(n, touch.value)
    time.sleep(0.1)



