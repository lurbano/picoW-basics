# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
import time
from math import sin
from math import pi
from random import randint
from ledPixelsPico import *

class sparkle:
    def __init__(self, n=0, duration=1):
        self.startTime = time.monotonic()
        self.duration = duration
        self.n = n
        self.time = 0.0
    def getColor(self):
        c = 10 * sin(pi*self.time/self.duration)
        return c
    
        
nPix = 36
ledPix = ledPixels(nPix, board.GP0)
dt = 0.01
duration = 0.1
addDt = 0.01


ledPix.brightness = 0.1
#ledPix.rainbow()
ledPix.setColor((0,0,0))

deleteList = []

sparkleList = [sparkle(2)]

addTime = 0.0

while True:
    for i in range(len(sparkleList)):
        #print(len(sparkleList), i)
        s = sparkleList[i]
        s.time += dt
        if s.time < s.duration:
            c = s.getColor()
            ledPix.light(s.n, (c,c,c))
            #print(s.time, s.getColor())
        else:
            #print("done", s.n)
            deleteList.append(i)
            
    for i in deleteList:
        #print("deleting ", i)
        del sparkleList[i]
    deleteList = []
            
    addTime += dt
    if addTime > addDt:
        n = randint(0, nPix-1)
        print("Adding:", n)
        sparkleList.append(sparkle(n))
        addTime = 0.0
        
    
    time.sleep(dt)
            
    

