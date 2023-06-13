# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio
from ledPixelsPico import *


ledPix = ledPixels(24, board.GP0)

ledPix.clear()
                    
print("hello")      
                
                
touchPins = [board.GP16, board.GP17, board.GP18, board.GP19]
touches = []
for pin in touchPins:
    touches.append(touchio.TouchIn(pin))
#touch = touchio.TouchIn(touch_pad)

n = 0

while True:
#     for touch in touches:
#         if touch.value:
#             ledPix.rainbow(speed=0.005)
#         else:
#             ledPix.clear()
            
    if touches[0].value:
        ledPix.setColor((100,0,0))
    if touches[1].value:
        ledPix.setColor((0,100,0))
    if touches[2].value:
        ledPix.setColor((0,0,100))
    if touches[3].value:
        ledPix.setColor((0,0,0))





