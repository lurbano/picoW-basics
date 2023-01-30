
# Tests GET request
# * Queries Eve's fortune teller (php) and gets the response.
# * Sends "name=Doc" as a url parameter


import wifi
import socketpool
import ssl
import adafruit_requests

#REPLACE WITH WIFI DETAILS
ssid = "Wifipower"
password = "defacto1"

url = 'https://soriki.com/eve/fortune/fortune-json.php?name=Doc'


print("connecting")

wifi.radio.connect(ssid, password)

print("connected")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
print("My IP address is", wifi.radio.ipv4_address)


try:
    #  pings eve's fortune teller
    print("Fetching text from %s" % url)
    #  gets the quote from adafruit quotes
    response = requests.get(url)
    print("-" * 40)
    #  prints the response to the REPL
    print("Text Response: ", response.text)
    print("-" * 40)
    response.close()
except Exception as e:
    print("Error:\n", str(e))
    print("Resetting microcontroller in 10 seconds")
    time.sleep(10)
    microcontroller.reset()
