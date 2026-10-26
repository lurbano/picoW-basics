import time
import board
import digitalio


s = digitalio.DigitalInOut(board.GP26)

s.direction = digitalio.Direction.INPUT
s.pull = digitalio.Pull.DOWN

while True:
    if  s.value:
        print("ON")
    else:
        print("--OFF--")
    time.sleep(0.1)
