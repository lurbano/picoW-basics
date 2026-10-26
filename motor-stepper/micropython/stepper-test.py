# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-stepper-motor-micropython/

import stepper
from time import sleep

# Define the stepper motor pins
IN1 = 2
IN2 = 3
IN3 = 4
IN4 = 5

# Initialize the stepper motor
stepper_motor = stepper.HalfStepMotor.frompins(IN1, IN2, IN3, IN4)

# Set the current position as position 0
stepper_motor.reset()

try:
    while True:
        #Move 500 steps in clockwise direction
        stepper_motor.step(500)
        sleep(0.5) # stop for a while
        
        # Move 500 steps in counterclockwise direction
        stepper_motor.step(-500)
        sleep(0.5) # stop for a while
        
        # Go to a specific position (in steps)
        stepper_motor.step_until(2000)
        sleep(0.5) # stop for a while
        
        # Force a direction using the dir paramter
        stepper_motor.step_until(2000, dir=-1)
        sleep(0.5) # stop for a while        
        
        # Go to a specific position (angle, maximum is 359, otherwise it will spin indefinetely)
        stepper_motor.step_until_angle(359)
        sleep(0.5) # stop for a while
    
except KeyboardInterrupt:
    print('Keyboard interrupt')
