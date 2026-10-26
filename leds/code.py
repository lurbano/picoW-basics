# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel

pixels = neopixel.NeoPixel(board.GP0, 20)

pixels[0] = (20,0,0)
pixels[-1] = (0,20,0)
