
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
from uSchedule import *
#from ledClock import *

# brightness Knob
brightness = 0.1


pixels = neopixel.NeoPixel(board.GP27, 20)
for i in range(20):
    pixels[i] = (0,20,0)

#ssid, password = secrets.WIFI_SSID, secrets.WIFI_PASSWORD  # pylint: disable=no-member
ssid, password = "TFS Students", "Fultoneagles"  # pylint: disable=no-member
wifi.radio.connect(ssid, password)
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)

# get time
ntp = adafruit_ntp.NTP(pool, tz_offset=0)
t = ntp.datetime
print("Time:", t)
print(f"Now: {t.tm_hour}:{t.tm_min}:{t.tm_sec}")


startTime = time.monotonic()
n = 0

while True:
    try:      
        # count seconds
        if (time.monotonic() - startTime) > 1:
            startTime = time.monotonic()
            n = n + 1
            print(n)
            
    except OSError as error:
        print(error)
        continue

        







