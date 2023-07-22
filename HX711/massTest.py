import time
import board
import digitalio
from HX711.hx711_gpio import HX711
# VSCodium Test

# setup pins
pin_OUT = digitalio.DigitalInOut(board.GP5)
pin_SCK = digitalio.DigitalInOut(board.GP6)
pin_SCK.direction = digitalio.Direction.OUTPUT

hx = HX711(pin_SCK, pin_OUT)
hx.OFFSET = 0 # -150000
hx.set_gain(128)
time.sleep(0.050)
scale = 25000.0

# get mass
mass = hx.read()/scale
print("Mass reading = {mass}")

############################
# tare (sets reads base data and resets the OFFSET)
#hx.tare()
