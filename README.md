# picoW-basics

Basic functions working with the Pi pico W - especially for wireless capabilities.

# Setup

Copy the file in the circuitpython folder (original source: https://circuitpython.org/board/raspberry_pi_pico_w/) to the Pico.
* It needs to be at least version 8.0.0 to have the capabilities for working with the wireless pico.

Copy the adafruit_requests file from the lib folder to the lib folder on the pico.


# Files and Folders

* internet_GET.py: 
** Queries Eve's fortune teller (php) and gets the response.
** Sends "name=Doc" as a url parameter

* HX711
** Code and library for weight/mass sensor
** https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/

