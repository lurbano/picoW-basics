import wifi
import socketpool
import ssl
import adafruit_requests
import time
import microcontroller

class GETLogger:
    def __init__(self, ssid, password, server="http://makerspace.local/logger/logger.php"):

        self.server = server 
        print("connecting")

        wifi.radio.connect(ssid, password)

        print("connected")

        self.pool = socketpool.SocketPool(wifi.radio)
        self.requests = adafruit_requests.Session(self.pool, ssl.create_default_context())

        print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
        print("My IP address is", wifi.radio.ipv4_address)

    def log(self, dataDict):
        # dataDict is a dictionary with information to be sent e.g.:
        #     dataDict = {"sensor": "T", "reading": "5", "units":"C"}

        # assemble get request 
        url = self.server + "?"
        for key, val in dataDict.items():
            url += f"{key}={val}&"
        url = url[:-1]
            
#         print("url: ", url)
#         response = self.requests.get(url)
#         print(response.text)
#         print("-" * 40)
#         response.close()

        try:
            print("url: ", url)
            response = self.requests.get(url)
            print(response.text)
            print("-" * 40)
            response.close()
        except Exception as e:
            print("Error:\n", str(e))
            print("Resetting microcontroller in 10 seconds")
            time.sleep(10)
            microcontroller.reset()


