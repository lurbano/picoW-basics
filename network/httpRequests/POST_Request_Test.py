'''
Reference: adafruit-circuitpython-bundle-8.x-mpy*/examples/requests_https_circuitpython.py
'''

import wifi
import socketpool
import adafruit_requests as requests
import json

ssid, password = "Wifipower", "defacto1"  # pylint: disable=no-member

print("Connecting to", ssid)
wifi.radio.connect(ssid, password)
print("Connected to", ssid)

pool = socketpool.SocketPool(wifi.radio)
http = requests.Session(pool)

data = {}
data["action"] = "Rhythmbox"
data["value"] = "play"

response = http.post("http://192.168.1.142:8000", data=json.dumps(data))
print(response.text)

