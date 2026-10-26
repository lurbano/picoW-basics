import board
import digitalio
import time
import neopixel

class IR:
    def __init__(self, IR_GP = board.GP28, LED_GP = board.GP22, startTime=time.monotonic()):
        self.break_beam = digitalio.DigitalInOut(IR_GP)
        self.break_beam.direction = digitalio.Direction.INPUT
        self.break_beam.pull = digitalio.Pull.UP
        
        self.pixels = neopixel.NeoPixel(LED_GP, 1)
        self.pixels[0] = (20,0,0)
        
        time.sleep(0.5)
        print(self.break_beam.value)
        if self.break_beam.value:
            self.pixels[0] = (0,20,0)
            
        self.startTime = startTime
        self.startFlag = False
        self.senseStart = -1.0
        self.senseEnd = -1.0
        self.senseDuration = -1.0
        
    def monitorLED(self):
        if self.break_beam.value:
            self.pixels[0] = (0,20,0)
        else:
            self.pixels[0] = (20,0,0)
            
    def monitor(self):
        self.monitorLED()
        if (not self.startFlag) and (not self.break_beam.value):
            self.senseStart = time.monotonic()
            self.startFlag = True
        if (self.startFlag) and (self.break_beam.value):
            self.senseDuration = time.monotonic() - self.senseStart
            self.startFlag = False
            return True
        return False
        
startTime = time.monotonic()

gate1 = IR(IR_GP = board.GP28, LED_GP = board.GP22, startTime = startTime)

print('done setup')

while True:
    #gate1.monitorLED()
    if gate1.monitor():
        print(f'Start: {gate1.senseStart-startTime}, Duration: {gate1.senseDuration}')


        

