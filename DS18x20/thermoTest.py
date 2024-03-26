'''
Temperature Sensor

Ref: Circuit diagram:
    https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-circuitpython/hardware

    Code: https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-circuitpython/circuitpython

      - 3.3V        -|
    (|- Data GPIO   -| 4.7 k Ohm Resistor
      - Gnd
'''

from uDS18x20 import *

thermo = uDS18X20(board.GP5)

T = thermo.read()

print(f"Temperature = {T}")

