# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio
from ledPixelsPico import *

touch_pad = board.GP16  
# touch_pad = board.A1  # For Circuit Playground Express

ledPix = ledPixels(12, board.GP0)




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
        ledPix.light(1,  (100,0,0))
    else:
        ledPix.light(1,  (0,0,0))
    if touches[1].value:
        ledPix.light(2,  (100,0,0))
    else:
        ledPix.light(2,  (0,0,0))
    if touches[2].value:
        ledPix.light(3,  (100,0,0))
    else:
        ledPix.light(3,  (0,0,0))
    if touches[3].value:
        ledPix.light(4,  (100,0,0))
    else:
        ledPix.light(4,  (0,0,0))





