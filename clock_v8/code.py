
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
from uNetComm import *
from uSchedule import *
from ledClock import *

# brightness Knob
brightness = 1.0

#ssid, password = secrets.WIFI_SSID, secrets.WIFI_PASSWORD  # pylint: disable=no-member
ssid, password = "TFS Students", "Fultoneagles"  # pylint: disable=no-member

pool = uNetConnect(ssid, password)
server = HTTPServer(pool)
# get time
#ntp = adafruit_ntp.NTP(pool, tz_offset=0)
clock = ledClock(board.GP27, 20, pool, True)
clock.initTime()
    

print(f"Listening on http://{wifi.radio.ipv4_address}:80")
# Start the server.
server.start(str(wifi.radio.ipv4_address))

while True:
    try:      
        dtime = time.monotonic() - clock.zeroTime
        clock.now = clock.startTime.addSecs(dtime)
        #print(dtime, clock.now)
        clock.lightToTime(clock.now)
            
    except OSError as error:
        print(error)
        continue

        







