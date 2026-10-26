import board
import digitalio
import time

break_beam = digitalio.DigitalInOut(board.GP18)
break_beam.direction = digitalio.Direction.INPUT
break_beam.pull = digitalio.Pull.UP
break_beam.value

gp18Flag = True
gp18Start = -1.0

while True:
    #print(break_beam.value)
    if gp18Flag and (not break_beam.value):
        gp18Flag = False
        gp18Start = time.monotonic()
        
    if (not gp18Flag) and break_beam.value:
        gp18Flag = True
        gp18Time = time.monotonic() - gp18Start
        break
    
print("GP18 Time:", gp18Time)
        
        
