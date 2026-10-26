import board
import asyncio
import time
import digitalio

# Reference: https://ben.akrin.com/?p=9768
# Required Libraries:
#   - asyncio
#   - adafruit_ticks


def moveTwo(m1, m2, r=8):
    for i in range(int(4096/r)):
        m1.stepRotate(nsteps=r)
        m2.stepRotate(nsteps=r)
        # time.sleep(0.001)
        
class twoMotors:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def move(self, nRot=1, d1="clockwise", d2="counterClockwise"):
        r=8
        nSteps = int(4096*nRot/r)
        for i in range(nSteps):
            if d1 == "clockwise" or d1 == "counterClockwise":
                self.m1.stepRotate(nsteps=r, direction=d1)
            if d2 == "clockwise" or d2 == "counterClockwise":
                self.m2.stepRotate(nsteps=r, direction=d2)
        self.m1.cleanup()
        self.m2.cleanup()
        
    def forward(self, nRot):
        self.move(nRot = nRot)
        
    def backward(self, nRot):
        self.move(nRot = nRot, d1="counterClockwise", d2="clockwise")
        
    def spinLeft(self, nRot):
        self.move(nRot = nRot, d1="counterClockwise", d2="counterClockwise")
        
    def spinRight(self, nRot):
        self.move(nRot = nRot, d1="clockwise", d2="clockwise")
        
    def pivotLeft(self, nRot):
        self.move(nRot=nRot, d1 = None, d2="counterClockwise")
    def pivotRight(self, nRot):
        self.move(nRot=nRot, d1 = "clockwise", d2=None)
        
    


class motorU:

    def __init__(self, in1=board.GP2, in2=board.GP3, in3=board.GP4, in4=board.GP5,
                 step_sleep=0.001,
                 trigT=32.):

        # number of steps required for 360 degree turn
        self.step_360 = int(4096)
        self.din1 = digitalio.DigitalInOut(in1)
        self.din2 = digitalio.DigitalInOut(in2)
        self.din3 = digitalio.DigitalInOut(in3)
        self.din4 = digitalio.DigitalInOut(in4)

        self.step_sleep = step_sleep

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        self.step_sequence = [[1, 0, 0, 1],
                              [1, 0, 0, 0],
                              [1, 1, 0, 0],
                              [0, 1, 0, 0],
                              [0, 1, 1, 0],
                              [0, 0, 1, 0],
                              [0, 0, 1, 1],
                              [0, 0, 0, 1]]

        # initialize Pins
        self.din1.direction = digitalio.Direction.OUTPUT
        self.din2.direction = digitalio.Direction.OUTPUT
        self.din3.direction = digitalio.Direction.OUTPUT
        self.din4.direction = digitalio.Direction.OUTPUT

        self.din1.value = False
        self.din2.value = False
        self.din3.value = False
        self.din4.value = False

        self.motor_pins = [self.din1, self.din2, self.din3, self.din4]

        # for greenhouse
        self.trigT = trigT
        self.windowOpen = False

    def cleanup(self):
        self.din1.value = False
        self.din2.value = False
        self.din3.value = False
        self.din4.value = False

    def stepRotate(self, nsteps=16, direction="clockwise"):
        motor_step_counter = 0
        for i in range(nsteps):
            for pin in range(0, len(self.motor_pins)):
                self.motor_pins[pin].value = self.step_sequence[motor_step_counter][pin]
            if direction == "clockwise":
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction == "counterClockwise":
                motor_step_counter = (motor_step_counter + 1) % 8

            time.sleep(self.step_sleep)

    def rotate(self, nRotations=1, direction="clockwise"):
        nsteps = int(self.step_360 * nRotations)
        motor_step_counter = 0
        for i in range(nsteps):
            for pin in range(0, len(self.motor_pins)):
                self.motor_pins[pin].value = self.step_sequence[motor_step_counter][pin]
            if direction == "clockwise":
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction == "counterClockwise":
                motor_step_counter = (motor_step_counter + 1) % 8

            time.sleep(self.step_sleep)

    async def aRotate(self, nRotations=1, direction="clockwise"):
        nsteps = int(self.step_360 * nRotations)
        motor_step_counter = 0
        for i in range(nsteps):
            for pin in range(0, len(self.motor_pins)):
                self.motor_pins[pin].value = self.step_sequence[motor_step_counter][pin]
            if direction == "clockwise":
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction == "counterClockwise":
                motor_step_counter = (motor_step_counter + 1) % 8

            await asyncio.sleep(self.step_sleep)
            # time.sleep(self.step_sleep)

    # async def aRotate(self, nRotations=1, direction="clockwise"):
    #     nsteps = int(self.step_360 * nRotations)
    #     motor_step_counter = 0
    #     for i in range(nsteps):
    #         for pin in range(0, len(self.motor_pins)):
    #             GPIO.output( self.motor_pins[pin], self.step_sequence[motor_step_counter][pin])
    #         if direction=="clockwise":
    #             motor_step_counter = (motor_step_counter - 1) % 8
    #         elif direction == "counterClockwise":
    #             motor_step_counter = (motor_step_counter + 1) % 8

    #         await asyncio.sleep(self.step_sleep)

    def openWindow(self):
        # just because that's my current physical design
        self.rotate(direction="counterClockwise")
        self.windowOpen = True

    # async def aOpenWindow(self):
    #     await self.aRotate(direction="counterClockwise") #just because that's my current physical design
    #     self.windowOpen = True

    def closeWindow(self, direction=True):
        # just because that's my current physical design
        self.rotate(direction="clockwise")
        self.windowOpen = False

    # async def aCloseWindow(self, direction=True):
    #     await self.aRotate(direction="clockwise")  #just because that's my current physical design
    #     self.windowOpen = False

    def setTrigT(self, T):
        self.trigT = float(T)

    # async def aTControl(self, sensor, dt = 60):
    #     # sensor is the temperature sensor instance of sensor_T
    #     print(f"Greenhouse Window Control On ({self.trigT})")
    #     self.TControlOn = True
    #     while self.TControlOn:
    #         T = await sensor.aRead_basic()
    #         if T > self.trigT and self.windowOpen == False:
    #             print("OPENING WINDOW")
    #             await self.aOpenWindow()

    #         elif T < self.trigT and self.windowOpen:
    #             print("CLOSING WINDOW")
    #             await self.aCloseWindow()

    #         await asyncio.sleep(dt)