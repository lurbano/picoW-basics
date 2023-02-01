# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

#  function to convert celcius to fahrenheit
def c_to_f(temp):
    temp_f = (temp * 9/5) + 32
    return temp_f

# thermometer class
class uDS18X20:
    def __init__(self, dataPin = board.GP5, units="C"):
        # keep track of units
        self.units = units

        # one-wire bus for DS18B20
        self.ow_bus = OneWireBus(dataPin)

        # scan for temp sensor
        self.ds18 = DS18X20(self.ow_bus, self.ow_bus.scan()[0])


    def read(self):

        T = self.ds18.temperature
        if self.units == "F":
            return c_to_f(T)
        else:
            return T


    def log_to_file(self, fname="log.dat", dt=5):
        startTime = time.monotonic() 
        mesTime = startTime

        while True:
            try:
                currentTime = time.monotonic()
                if (mesTime + dt) >= currentTime:
                    mesTime = currentTime
                    T = self.read()
                    runTime = mesTime - startTime
                    print(runTime, T)
                    with open(fname, "a") as logFile:
                        logFile.write(f'{runTime},{T}')
                    
            except Exception:
                continue

    def log_to_server(self, server="http://makerspace.local/TLog.php", dt=5):
        startTime = time.monotonic() 
        mesTime = startTime

        while True:
            try:
                currentTime = time.monotonic()
                if (mesTime + dt) >= currentTime:
                    mesTime = currentTime
                    T = self.read()
                    runTime = mesTime - startTime
                    print(runTime, T)
                    
                    
            except Exception:
                continue


