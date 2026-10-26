
import socketpool
import wifi

from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPServer
import adafruit_ntp

import board
import time
from ledPixelsPico import *
import neopixel

from uNetComm import *
from uSchedule import *
from ledClock import *

# brightness Knob
brightness = 0.1

#ssid, password = secrets.WIFI_SSID, secrets.WIFI_PASSWORD  # pylint: disable=no-member
ssid, password = "TFS Students", "Fultoneagles"  # pylint: disable=no-member

print("Connecting to", ssid)
wifi.radio.connect(ssid, password)
print("Connected to", ssid)

pool = socketpool.SocketPool(wifi.radio)

# get time
#ntp = adafruit_ntp.NTP(pool, tz_offset=0)
startTime = getNTP_Time(pool)
now = startTime
print("Start Time: ", startTime, startTime.hr, startTime.min, startTime.sec)

# leds
clock = ledClock(board.GP27, 20, pool, True)
clock.initTime()
    

# Start the server.

while True:
    try:      
        dtime = time.monotonic() - clock.zeroTime
        clock.now = clock.startTime.addSecs(dtime)
        #print(dtime, clock.now)
        clock.lightToTime(clock.now)
            
    except OSError as error:
        print(error)
        continue






