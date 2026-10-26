from ledPixelsPico import *


class ledRound(ledPixels):

    def __init__(self, ledPin=board.GP0, nPix=76
                ):
        ledPixels.__init__(self, nPix=nPix, ledPin=ledPin)
        