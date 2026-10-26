import wifi
import socketpool
import adafruit_requests as requests
import json
import time




class uNetComm:
    def __init__(self, pool = None):
        if pool == None:
            raise Exception("U Error: connection to network (try netConnect())")
                  
        self.http = requests.Session(pool)
        self.IPs = {}
        self.IPs['bedroomSpeaker'] = '192.168.1.142:8000'
        self.IPs['kitchen'] = '192.168.1.131:80'

    def request(self, addr, action, value=""):
        # check if addr is string in self.IPs list
        for key in self.IPs:
            if addr == key:
                addr = f"http://{self.IPs[key]}"
                break
        
        data = {}
        data["action"] = action
        data["value"] = value
        
        response = self.http.post(addr, data=json.dumps(data))
        print(response.text)
        return response
        
def uNetConnect(ssid="Wifipower", password="defacto1"):

    print("Connecting to", ssid)
    wifi.radio.connect(ssid, password)
    print("Connected to", ssid)

    pool = socketpool.SocketPool(wifi.radio)
    
    return pool

if __name__ == '__main__':
    pool = uNetConnect()
    comm = uNetComm(pool)
    
    #comm.request("http://192.168.1.142:8000", "Rhythmbox", "play")
    comm.request("bedroomSpeaker", "Rhythmbox", "play")
    time.sleep(5)
    comm.request("http://192.168.1.142:8000", "Rhythmbox", "pause")
    
    
