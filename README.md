# picoW-basics

Basic functions working with the Pi pico W - especially for wireless capabilities.

# Setup

Install Circuitpython (PicoW):
* Download and copy the circuitpython uf2 to the Pico from:
    * https://circuitpython.org/board/raspberry_pi_pico_w/
* It needs to be at least version 8.0.0 to have the capabilities for working with the wireless pico.
* Note: For Pico (not wireless, but code not requiring networking will work on the Picos):
    * https://circuitpython.org/board/raspberry_pi_pico/

Copy the adafruit_requests file from the lib folder to the lib folder on the pico.
* adafruit_requests.mpy
** which is in the bundle: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
** Note: get the 8.x version to match the circuitpython version.
* adafruit_httpserver:
** get version 8 from: https://github.com/adafruit/Adafruit_CircuitPython_HTTPServer/releases/tag/2.3.1


# Files and Folders

---

**pico/**: files for the pico. Used to send requests (GET so far) to a server.
* **internet_GET.py**: 
    * Queries Eve's fortune teller (php) and gets the response.
    * Sends "name=Doc" as a url parameter
    * requires adafruit_requests.py (in the lib directory)
* **GETLogger.py**:
    * Class for making logging data to the server (logging/logger.php) easier. 
    * Usage example in DS18x20/thermoLogToServer.py
* **serverTest.py**
    * Serves basic webpage and checks every 30 seconds to see if it's still connected to the internet.
**serverTest2.py**
    * Serves basic webpage with buttons to turn the picoW's onboard led ON and OFF.
* **serverTest-xml.py**
    * Control the onboard led via a button on the webpage using xmlHTTPRequest

---

**logging/**: Log data coming in from a picoW with a picoID
* **Server side**
    * **logger.php**: accepts GET requests (example usage: DT18x20/thermoLogToServer.py) and logs all info (plus time) to a file named based on the picoID sent (pico_{picoID}.json).
* **Client side**
    * **picoSensorDB.js**: class that fetches the data from the server for display.
    * **showData.html**: Reads data for the given picoID from the serverand displays as a table. Refreshes every second.

---

**DS18x20/**: **Temperature sensor** (and logging)
* **uDS18x20.py**
    * Class for using a DS18x20 temperature sensor
    * The default data pin is board.GP5
    * Add from lib/
        * adafruit_ds18x20.mpy
        * adafruit_onewire
        * adafruit_bus_device
* **thermoLogToServer.py**: Program for picoW that sends data to the server (logger/logger.php) as a GET request every so often (dt).
    * Uses GETLogger class (in GEtLogger.py)
    * Assembles data to be sent in a dictionary called **data**.

---

**HX711/**: **Force/Mass sensor**
* Code and library for weight/mass sensor
* **hx711_gpio.py** library from: https://github.com/Miakatt/Hx711_circuitpython/blob/main/hx711_gpio.py
    * Original?: https://github.com/robert-hh/hx711/blob/master/hx711_gpio.py
* Wiring: https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/
    * load sensor to hx711: The load sensor has 4 wires.
        * Red to E+
        * Black to E-
        * Green to A-
        * White to A+
    * hx711 to picoW: 
        * VCC to VBUS (5V)
        * GND to GND (any one)
        * DT to GP5 (GPIO 5 but can be changed)
        * SCK to GP6 (GPIO 6 but can be changed)
* will need to be calibrated with known masses
* **massTest.py**: testing the sensor and hx711_gpio.py class (not calibrated so just gets the raw output from sensor).


**Audio**:
* Reference (adafruit): https://learn.adafruit.com/mp3-playback-rp2040/pico-mp3
---
