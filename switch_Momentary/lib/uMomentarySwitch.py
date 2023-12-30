import board
import digitalio
import time

'''
Connections:

  Power: 3V
  Data: any GPIO
'''

class uMomentarySwitch:
    
    def __init__(self, pin = board.GP19):
        self.switch = digitalio.DigitalInOut(board.GP19)
        self.switch.direction = digitalio.Direction.INPUT
        self.switch.pull = digitalio.Pull.DOWN
        
    def getValue(self):
        return self.switch.value
    
    def switchCheck(self):
        if self.switch.value:
            while self.switch.value:
                time.sleep(0.1)
            return True
        else:
            return False

if __name__ == '__main__':
    pin = board.GP19
    s = uMomentarySwitch(board.GP19)
    print("Testing Momentary Switch at:", pin)
    n = 0
    while True:
        if s.switchCheck():
            n += 1
            print(f"{n}: Pressed and Released")
        time.sleep(0.1)
        
