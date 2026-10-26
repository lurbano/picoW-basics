# runs for runTime with a little buzz when the switch is 
#  turned on and a longer one when it's turned off
# Vibration motor and switch connected to 3.3V


import board
import time
import digitalio
import simpleio

timerBtn = digitalio.DigitalInOut(board.GP9)
timerBtn.pull = digitalio.Pull.DOWN

l_timer = False
l_start = True

runTime = 60  # seconds
dt = 0

while True:
    if timerBtn.value:
        if not l_timer and l_start: #Turn on timer
            l_timer = True
            l_start = False
            startTime = time.monotonic()
            print("Starting")
            simpleio.tone(board.GP1, 440, 0.25)
        
        if l_timer:
            dt = time.monotonic() - startTime
            if dt > runTime:
                l_timer = False
                simpleio.tone(board.GP1, 440, 1)
                
    else:
        l_timer = False
        l_start = True
    time.sleep(0.1)
    print(l_timer, dt)
