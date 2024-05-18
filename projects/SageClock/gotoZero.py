from motorU import *
from uSchedule import *
rightMotor = motorU(in1=board.GP8, in2=board.GP9, in3=board.GP10, in4=board.GP11)
leftMotor = motorU(in1=board.GP0, in2=board.GP1, in3=board.GP2, in4=board.GP3)

def fivemin():
    rightMotor.stepRotate(342,"clockwise")
def anhour():
    leftMotor.stepRotate(342,"clockwise")

def backhour():
    leftMotor.stepRotate(342,"counterClockwise")


def gototime(h,m):
    for i in range(int(m/5)):
        fivemin()
    for i in range(h):
        anhour()

def gotoZero(h,m):
    n=12-round(m/5)
    for i in range (n):
        print("minutes: ",i)
        fivemin()
    y=-h+12
    for i in range(y):
        anhour()
        print("hour: ",i)
        
def backfivemin():
    rightMotor.stepRotate(342,"counterClockwise")
    
gotoZero(4,15) 
    
rightMotor.cleanup()
leftMotor.cleanup()


