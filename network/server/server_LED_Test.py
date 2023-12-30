# SPDX-FileCopyrightText: 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

#import secrets  # pylint: disable=no-name-in-module

import socketpool
import wifi

from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPServer

import neopixel
import json
import board
from digitalio import DigitalInOut, Direction



#ssid, password = secrets.WIFI_SSID, secrets.WIFI_PASSWORD  # pylint: disable=no-member
ssid, password = "Wifipower", "defacto1"  # pylint: disable=no-member

print("Connecting to", ssid)
wifi.radio.connect(ssid, password)
print("Connected to", ssid)

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)

def webpage():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PicoW Test Server</title>
</head>
<body>
    Pico W here.
    
    <div id="data">Hi</div>

    <input type="button" id="led" value="LED">

    <input type="button" id="Temperature" value="Get Temperature">
    <span id="Tmp"></span>
    
</body>
<script>
    d = document;

    ledStatus = "OFF";
    ledButton = d.getElementById("led");
    ledButton.addEventListener("click", makeRequest);

    function makeRequest() {
        console.log("making request")
        let xR = new XMLHttpRequest();
        xR.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                
                console.log("Server Response:", this.responseText);
                data = JSON.parse(this.responseText);
                ledButton.value = data['status'] ? "ON" : "OFF";
            }
        }
        let data = {};
        ledStatus = ledStatus === "OFF" ? "ON" : "OFF";
        data["action"] = ledStatus;
        xR.open("POST", "led", true);
        xR.send(JSON.stringify(data));
    }

</script>
</html>
    """
    return html

def requestToArray(request):
    raw_text = request.body.decode("utf8")
    print("Raw")
    data = json.loads(raw_text)
    return data

@server.route("/")
def base(request: HTTPRequest):
    """
    Serve the default index.html file.
    """
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = False
@server.route("/led", "POST")
def ledButton(request: HTTPRequest):
    # raw_text = request.body.decode("utf8")
    print("Raw")
    # data = json.loads(raw_text)
    data = requestToArray(request)
    print(f"data: {data} & action: {data['action']}")
    rData = {}
    
    if (data['action'] == 'ON'):
        led.value = True
        
    if (data['action'] == 'OFF'):
        led.value = False
    
    rData['item'] = "led"
    rData['status'] = led.value
        
    with HTTPResponse(request) as response:
        response.send(json.dumps(rData))
 

print(f"Listening on http://{wifi.radio.ipv4_address}:80")
server.serve_forever(str(wifi.radio.ipv4_address))


        
