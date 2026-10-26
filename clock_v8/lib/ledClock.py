from ledPixelsPico import *
from uSchedule import *
from uNetComm import *
import time

class ledClock(ledPixels):
    def __init__(self, ledPin=board.GP15, nPix = 72, pool = None, reverse=True):
        
        ledPixels.__init__(self, nPix=nPix, ledPin=ledPin)
        
        self.nPix = nPix
        self.pool = pool
        self.reverse = reverse
        self.hCol = (200,0,0)
        self.mCol = (0,200,0)
        self.sCol = (0,0,200)
        
        self.off()
        

    def initTime(self):
        self.startTime = self.getTimeNTP()
        self.zeroTime = time.monotonic()
        self.now = self.startTime
        print("uClock Start Time: ", self.startTime)
        
        
    def runClock(self):
        t = time.monotonic()
        while True:
            dt = time.monotonic() - t
            if dt >= 1:
                self.now = self.now.addSecs(dt)
                self.lightToTime(self.now)
                t = time.monotonic()
            
        
    def getTimeNTP(self):
        now = getNTP_Time(self.pool)
        return now
    
     
    def lightToTime(self, t = uTime("9:30:15")):
        nHr = int((t.hr%12)/12 * self.nPix) 
        nMn = int(t.min/60 * self.nPix)
        nSc = int(t.sec/60 * self.nPix)
        
        #print("nHr, nMn, nSc: ", nHr, nMn, nSc)
        
        if self.reverse:
            for i in range(self.nPix):
                if i > (self.nPix - nHr):
                    self.pixels[i] = self.hCol
                else:
                    self.pixels[i] = (0,0,0)
            self.pixels[self.nPix - nMn - 1] = self.mCol
            self.pixels[self.nPix - nSc - 1] = self.sCol
            
        else:
        
            for i in range(nHr):
                self.pixels[i] = self.hCol
            for i in range(nHr,self.nPix):
                self.pixels[i] = (0,0,0)
                
            self.pixels[nMn] = self.mCol
            self.pixels[nSc] = self.sCol

        self.show()
        
    def lightToTimeOld(self, t = uTime("9:30:15")):
        nHr = int((t.hr%12)/12 * self.nPix) 
        nMn = int(t.min/60 * self.nPix)
        
        print("nHr, nMn: ", nHr, nMn)
        
        if self.reverse:
            for i in range(self.nPix-1, self.nPix-nHr-1, -1):
                self.pix.light(i, self.hCol)
            for i in range(self.nPix-1, self.nPix-nMn-1, -1):
                self.pix.light(i, self.mCol)
                
        else:
            for i in range(nHr):
                self.pix.light(i, self.hCol)
            for i in range(nMn):
                self.pix.light(i, self.mCol)
                   
        
    def lightSec(self, t = uTime("9:30:15")):
        nSc = int(t.sec/60 * self.nPix)
        self.pixels[nSc] = self.sCol
        self.show()
        
    
if __name__ == "__main__":
    print("Hi")
    ssid, password = "TFS Students", "Fultoneagles"  # pylint: disable=no-member
    pool = uNetConnect(ssid, password)
    
    clock = ledClock(board.GP17, 72, pool, True)
    clock.initTime()
    clock.runClock()
    
    print(time.monotonic())
    time.sleep(1)
    print(time.monotonic())