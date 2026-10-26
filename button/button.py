# Get signal from a button
# one pole to 3.3V and one to a GP pin

import board
import time
import digitalio

timerBtn = digitalio.DigitalInOut(board.GP9)
timerBtn.pull = digitalio.Pull.DOWN

while True:
    if timerBtn.value:
        print("ON")
    else:
        print("OFF")
    time.sleep(0.1)
