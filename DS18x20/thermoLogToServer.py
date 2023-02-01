from DS18x20.uDS18x20 import *
from GETLogger import *
import time

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
logger = GETLogger("TFS", "3144696622", "http://popu.local/logger/logger.php")

# data["reading"] = str(thermo.read())
# print("data:", data)
# logger.log(data)


startTime = time.monotonic() 
mesTime = startTime
while True:
    try:
        data["reading"] = str(thermo.read())
        print("reading", data["reading"])
        logger.log(data)
        time.sleep(dt)
            
    except Exception as e:
            print("Error:\n", str(e))
            #continue

