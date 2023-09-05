# Get signal from a button

import board
import time
from digitalio import DigitalInOut, Direction, Pull

timerBtn = DigitalInOut(board.GP19)
timerBtn.direction = Direction.INPUT
timerBtn.pull = Pull.UP

while True:
    if timerBtn.value:
        print("ON")
    else:
        print("OFF")
    time.sleep(0.1)
