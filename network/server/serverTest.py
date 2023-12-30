# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import time
import ipaddress
import wifi
import socketpool
import busio
import board
import microcontroller


from digitalio import DigitalInOut, Direction
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.methods import HTTPMethod
from adafruit_httpserver.mime_type import MIMEType
#from adafruit_onewire.bus import OneWireBus
#from adafruit_ds18x20 import DS18X20

#  onboard LED setup
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = False


# one-wire bus for DS18B20
#ow_bus = OneWireBus(board.GP6)

# scan for temp sensor
#ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

#  function to convert celcius to fahrenheit
#def c_to_f(temp):
#    temp_f = (temp * 9/5) + 32
#    return temp_f


#  connect to network
print()
print("Connecting to WiFi")


#  set static IP address
ipv4 =  ipaddress.IPv4Address("192.168.1.42")
netmask =  ipaddress.IPv4Address("255.255.255.0")
gateway =  ipaddress.IPv4Address("192.168.1.1")
wifi.radio.set_ipv4_address(ipv4=ipv4,netmask=netmask,gateway=gateway)
#  connect to your SSID
#wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
wifi.radio.connect("Wifipower", "defacto1")

print("Connected to WiFi")
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)


#  the HTML script
#  setup as an f string
#  this way, can insert string variables from code.py directly
#  of note, use {{ and }} if something from html *actually* needs to be in brackets
#  i.e. CSS style formatting
def webpage():
    html = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PicoW Test Server</title>
</head>
<body>
    Pico W here.
</body>
</html>
    """
    return html

#  route default static IP
@server.route("/")
def base(request: HTTPRequest):  # pylint: disable=unused-argument
    #  serve the HTML f string
    #  with content type text/html
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")

#  if a button is pressed on the site
@server.route("/", method=HTTPMethod.POST)
def buttonpress(request: HTTPRequest):
    #  get the raw text
    raw_text = request.raw_request.decode("utf8")
    print(raw_text)
    #  if the led on button was pressed
    if "ON" in raw_text:
        #  turn on the onboard LED
        led.value = True
    #  if the led off button was pressed
    if "OFF" in raw_text:
        #  turn the onboard LED off
        led.value = False
    #  if the party button was pressed
    if "party" in raw_text:
        #  toggle the parrot_pin value
        parrot_pin.value = not parrot_pin.value
    #  reload site
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")

print("starting server..")
# startup the server
try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s:80" % wifi.radio.ipv4_address)
#  if the server fails to begin, restart the pico w
except OSError:
    time.sleep(5)
    print("restarting..")
    microcontroller.reset()
ping_address = ipaddress.ip_address("8.8.4.4")


clock = time.monotonic() #  time.monotonic() holder for server ping
parrot = False #  parrot state
party = 0 #  time.monotonic() holder for party parrot
p = 0 #  index for tilegrid

while True:
    try:
        #  every 30 seconds, ping server & update temp reading
        if (clock + 30) < time.monotonic():
            if wifi.radio.ping(ping_address) is None:
                print("lost connection")
            else:
                print("connected")
            clock = time.monotonic()
            #  comment/uncomment for desired units
        server.poll()
    # pylint: disable=broad-except
    except Exception as e:
        print(e)
        continue
