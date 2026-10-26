import board
from digitalio import DigitalInOut, Direction, Pull
import time

class u3WaySwitch:
    def __init__(self, pin1 = board.GP18, pin2 = board.GP19):
        self.s1 = DigitalInOut(pin1)
        self.s1.direction = Direction.INPUT
        self.s1.pull = Pull.DOWN

        self.s2 = DigitalInOut(pin2)
        self.s2.direction = Direction.INPUT
        self.s2.pull = Pull.DOWN
        
        self.state = self.getState()
        self.oldState = self.state
        
    def getState(self):
        if self.s1.value:
            self.state = 1
        elif self.s2.value:
            self.state = 2
        else:
            self.state = 0
        return self.state

    def change(self):
        l_change = False
        self.state = self.getState()
        if self.state != self.oldState:
            l_change = True
            self.oldState = self.state
        return l_change


# TEsting
if __name__ == '__main__':
    # 3 way switches
    doorSwitch = u3WaySwitch(pin1 = board.GP18, pin2 = board.GP19)

    while True:
        print(doorSwitch.getState())
        if doorSwitch.change():
            print("Changed to: ", doorSwitch.state)
        time.sleep(0.2)
        