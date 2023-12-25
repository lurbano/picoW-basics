import time
import board
from analogio import AnalogIn

'''
Ref: https://learn.adafruit.com/circuitpython-oled-knob-sketcher/reading-pots

Connections: (view from back)

  3V  Ain  G
   |   |   |
  -----------

  Ain - analog pin on the pico
'''

'''

knob = AnalogIn(board.A1)

while True:
    print((knob.value, ))
    time.sleep(0.2)
