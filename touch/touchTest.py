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

touch_pad = board.GP18 
touch = touchio.TouchIn(touch_pad)

                  
print("hello")      
                    

n = -1

while True:
    
    n += 1
    print(n, touch.value)
    time.sleep(0.1)




