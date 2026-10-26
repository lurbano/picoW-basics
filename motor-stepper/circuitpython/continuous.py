from motorU import *

# rotates continuously. Does not stop.

print("start")
motor = motorU(in1=board.GP9, in2=board.GP10, in3=board.GP11, in4=board.GP12, step_sleep=0.001)
print("done setup")

motor_step_counter = 0
direction = -1

while True:
    for pin in range(0, len(motor.motor_pins)):
        motor.motor_pins[pin].value = motor.step_sequence[motor_step_counter][pin]
    motor_step_counter = (motor_step_counter + direction) % 8
    

    time.sleep(0.005)
