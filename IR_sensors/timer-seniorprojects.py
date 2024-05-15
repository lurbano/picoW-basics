# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import time
import board
import neopixel
import touchio
import math

touch_pad = board.GP16 
touch = touchio.TouchIn(touch_pad)

nPix = 20
pixels = neopixel.NeoPixel(board.GP15, nPix)

pixels[-1] = (20,0,20)

def get_n(t):
    n = int(math.ceil(t/tFactor))
    return min(n, nPix)

# Time settings
tFactor = 60  # set to 60 for minutes
greenTime = 10 * tFactor
yellowTime = 2 * tFactor
redTime = 3 * tFactor

greenCol = (0, 40, 0)
yellowCol = (20, 20, 0)
redCol = (40, 0, 0)
baseCol = (0, 10, 10)

totalTime = greenTime + yellowTime + redTime
nGreen = get_n(greenTime)
nYellow = nGreen + get_n(yellowTime)
nRed = nYellow + get_n(redTime)

print("n:", nGreen, nYellow, nRed)

# startup sequence
for i in range(nPix):
    pixels[i] = (0,20,0)
    time.sleep(0.01)

try:
    startTime = time.monotonic()
    # clear strip
    for i in range(nPix):
        if i <= get_n(totalTime):
            pixels[i] = baseCol
        else:
            pixels[i] = (0,0,0)
            
    while True:
        runTime = time.monotonic() - startTime
        n = get_n(runTime)
        print("n: ", n)
        
        if n <= nRed:
            # light up
            for i in range(n):
                if i < nGreen:
                    pixels[i] = greenCol
                elif i < nYellow:
                    pixels[i] = yellowCol
                elif i < nRed:
                    pixels[i] = redCol
                else:
                    pixels[i] = baseCol
        elif n < nPix:
            
            nExtra = n - nRed
            print("nExtra: ", nExtra)
            for i in range(nExtra):
                    pixels[i] = (200,0,0)
                    
        else:
            for i in range(nPix):
                pixels[i] = (200,0,0)
                time.sleep(0.25)
                    
                
        time.sleep(1)
        
        
        
        if touch.value:
            pixels[-1] = (0,0,20)
        else:
            pixels[-1] = (20,0,0)
        time.sleep(0.1)
except:
    pixels[-1] = (40,0,0)
    print("Error")
    
