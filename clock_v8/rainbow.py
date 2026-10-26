# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
from ledPixelsPico import *


#pixels = neopixel.NeoPixel(board.GP21, 1)
#pixels[0] = (200,0,0)
#pixels[-1] = (0,20,0)
ring = ledPixels(128, board.GP15)
ring.brightness = 0.5
ring.rainbowForever(speed=0.1)
