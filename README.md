# picoW-basics

Basic functions working with the Pi pico W - especially for wireless capabilities.

# Setup

Copy the file in the circuitpython folder (original source: https://circuitpython.org/board/raspberry_pi_pico_w/) to the Pico.
* It needs to be at least version 8.0.0 to have the capabilities for working with the wireless pico.

Copy the adafruit_requests file from the lib folder to the lib folder on the pico.
* adafruit_requests.mpy
** which is in the bundle: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
** Note: get the 8.x version to match the circuitpython version.


# Files and Folders

* internet_GET.py: 
    * Queries Eve's fortune teller (php) and gets the response.
    * Sends "name=Doc" as a url parameter

* GETLogger.py:
    * Class for making logging data to the server (logging/logger.php) easier. 
    * Usage example in DS18x20/thermoLogToServer.py

* HX711/: **Force/Mass sensor**
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

* DS18x20: **Temperature sensor** (and logging)
    * uDS18x20
        * Class for using a DS18x20 temperature sensor
        * The default data pin is board.GP5
        * Add from lib/
            * adafruit_ds18x20.mpy
            * adafruit_onewire
            * adafruit_bus_device
    * thermoLogToServer.py: Program for picoW that sends data to the server (logger/logger.php) as a GET request every so often (dt).
        * Uses GETLogger class (in GEtLogger.py)
        * Assembles data to be sent in a dictionary called **data**.

* **logging/**: Log data coming in from a picoW with a picoID
    * logger.php: accepts GET requests and logs all info (plus time) to a file named based on the picoID sent (pico_{picoID}.json).
    * picoSensorDB.js: class that fetches the data from the server for display.
    * showData.html: Reads data for the given picoID from the serverand displays as a table. Refreshes every second.