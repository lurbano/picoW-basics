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
** Queries Eve's fortune teller (php) and gets the response.
** Sends "name=Doc" as a url parameter

* HX711
** Code and library for weight/mass sensor
** hx711_gpio.py library from: https://github.com/Miakatt/Hx711_circuitpython/blob/main/hx711_gpio.py
*** Original?: https://github.com/robert-hh/hx711/blob/master/hx711_gpio.py
** Wiring: https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/
** will need to be calibrated with known masses

* ThermoDS18x20
** Class for using a DS18x20 temperature sensor
** The default data pin is board.GP5
