import board
from analogio import AnalogIn

class photoResist:

    def __init__(self, pin=board.A0, maxVal=65535, minVal=256):
        self.knob = AnalogIn(pin)
        self.max = maxVal
        self.min = minVal

    def getValueFromPercent(self, pct=50):
        dp = (pct * (self.max-self.min)/100)
        # print(dp)
        val = self.min + dp
        if val > self.max:
            val  = self.max
        elif val < self.min:
            val = self.min
        return val
    
    def getPercent(self, val=None, reverse=True):
        if val == None:
            val = self.knob.value
        pct = 100 * (val -self.min)/(self.max-self.min)
        if pct > 100:
            pct = 100
        elif pct < 0:
            pct = 0
        if reverse:
            pct = 100-pct
        #print(val, pct)
        return(pct)
    
    def value(self):
        return self.knob.value
    
        
    

if __name__ == '__main__':
    knob = photoResist()
    p = 10
    print(p, knob.getValueFromPercent(p))
    print(knob.getPercent(255000), "%")

