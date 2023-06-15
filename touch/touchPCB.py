import time
import board
import touchio
from ledPixelsPico import *


leds = []
leds.append(ledPixels(5, board.GP20))
leds.append(ledPixels(5, board.GP18))

touches = []
touches.append(touchio.TouchIn(board.GP21))
touches.append(touchio.TouchIn(board.GP19))

n = 0

while True:
    for i in range(len(touches)):
        if touches[i].value:
            leds[i].setColor((0, 50, 0))

        else:
            leds[i].setColor((0, 0, 50))
    time.sleep(0.05)
