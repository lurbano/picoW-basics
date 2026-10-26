from motorU import *
rightMotor = motorU(in1=board.GP1, in2=board.GP2, in3=board.GP3, in4=board.GP4)
leftMotor = motorU(in1=board.GP9, in2=board.GP10, in3=board.GP11, in4=board.GP12)

moveTwo(rampMotor, leftMotor)
#leftMotor.rotate()