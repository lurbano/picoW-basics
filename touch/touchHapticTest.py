# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example
    Power: 3V
    Data: any GPIO
    Ground: Any
"""
import time
import board
import touchio
import simpleio

vibPin = board.GP15

touch_pad = board.GP3 
touch = touchio.TouchIn(touch_pad)

                  
print("hello")      
                    

n = -1

while True:
    
    n += 1
    print(n, touch.value)
    if touch.value:
        simpleio.tone(vibPin, 880, 0.25)
        time.sleep(0.5)
    time.sleep(0.1)




