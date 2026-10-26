import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import touchio
from ledPixelsPico import *

timerBtn = DigitalInOut(board.GP19)
timerBtn.direction = Direction.INPUT
timerBtn.pull = Pull.UP

nPix = 12
ledPix = ledPixels(nPix, board.GP16)

timerPix = 10  # number of pixels for the timer
               # this leaves 2 pixels for info

runTime = 20
warnTime = 10

mx = 100       # maximum light level

# TOUCH SENSORS
resetPin = board.GP11
resetTouch = touchio.TouchIn(resetPin)


def readyStatusLight():
    ledPix.pixels[-1] = (0, 0, mx)
    ledPix.show()

def pauseMode():
    ledPix.pixels[-1] = (mx, 0, 0)
    ledPix.show()
    startPause = time.monotonic()
    l_reset = False
    while timerBtn.value:
        while resetTouch.value:
            l_reset = True
            lightUp(timerPix, (0,mx,0))
        time.sleep(0.1)
    readyStatusLight()
    if l_reset:
        return time.monotonic()
    else:
        pauseTime = time.monotonic() - startPause
        return pauseTime + startTime

def lightUp(n, col):
    for i in range(timerPix):
        if i < n:
            ledPix.pixels[i] = col
        else:
            ledPix.pixels[i] = (0,0,0)
    ledPix.show()

startTime = time.monotonic()
readyStatusLight()


while True:
    while resetTouch.value:
        startTime = time.monotonic()
        time.sleep(0.1)
    
    if timerBtn.value:
        startTime = pauseMode()
    else:
        print("ON")
        timeSoFar = time.monotonic() - startTime
        if timeSoFar < runTime:
            nGreen = int(timerPix * ((runTime-timeSoFar)/ runTime))
            lightUp(nGreen, (0,mx,0))
        else:
            overTime = timeSoFar - runTime
            nWarn = int(overTime / 60) + 1
            warnCol = (mx, mx/2, 0)
            
            if overTime > warnTime:
                warnCol = (mx, 0, 0)
                
            lightUp(nWarn, warnCol)
            print("overTime", overTime, nWarn)
               
                
        
        print(timeSoFar, nGreen)
    time.sleep(0.1)
        
        
        
