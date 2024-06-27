import board
import time
import digitalio
from adafruit_motor import stepper

# requires adafruit_motor

in1=board.GP9
in2=board.GP10
in3=board.GP11
in4=board.GP12

DELAY = 0.005
STEPS = 2000

# To use with CircuitPython and a microcontroller:
coils = (
    digitalio.DigitalInOut(in1),  # A1
    digitalio.DigitalInOut(in2),  # A2
    digitalio.DigitalInOut(in3),  # B1
    digitalio.DigitalInOut(in4),  # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(DELAY)
    
motor.release()
