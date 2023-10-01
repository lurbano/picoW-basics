import time
import board
#import pwmio
import simpleio

#vib = pwmio.PWMOut(board.GP1, duty_cycle=0, frequency= 440, variable_frequency=True)

# vib.duty_cycle = 65535 // 2
# time.sleep(1)
# vib.duty_cycle = 0
# time.sleep(1)
# vib.duty_cycle = 65535 // 2
# time.sleep(1)
# vib.duty_cycle = 0
# time.sleep(1)

simpleio.tone(board.GP1, 440, 1)

print("hi")