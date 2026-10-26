import json
import time

data = {}
data["picoID"] = "chickens"
data["sensor"] = "T"
data["reading"] = ""
data["units"] = "C"


for i in range(20):
    data["reading"] = i 
    with open("testDB.json", "a") as f:
        f.write(json.dumps(data)+'\n')
    time.sleep(2)
