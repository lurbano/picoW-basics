from DS18x20.uDS18x20 import *
from GETLogger import *

# TIMESTEP
dt = 5 # seconds

# set up data structure
data = {}
data["picoID"] = "chickens"
data["sensor"] = "T"
data["reading"] = ""
data["units"] = "C"

# set up thermometer and test
thermo = uDS18X20(board.GP5, units=data["units"])
T = thermo.read()
print(f"Temperature = {T}")

# set up logger *** SET ssid AND password
logger = GETLogger("ssid", "password", "http://makerspace.local/logger.php")


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
            data["reading"] = T
            logger.log(data)
            
    except Exception:
        continue
