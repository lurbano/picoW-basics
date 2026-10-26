import time
import board
from photoResist import *

'''
Ref: https://learn.adafruit.com/circuitpython-oled-knob-sketcher/reading-pots

Connections: (view from back)

  3V  Ain  G
   |   |   |
  -----------

  Ain - analog pin on the pico
'''


pr = photoResist(board.A0, maxVal=48000, minVal=9000)  #GP26

while True:
    
    print(pr.value(), pr.getPercent())
    time.sleep(0.2)
