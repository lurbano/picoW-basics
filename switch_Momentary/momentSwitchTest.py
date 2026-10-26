import board
import digitalio
import time

'''
Connections:

  D1  3V  D2  
   |   |   |
  -----------
'''

s1 = digitalio.DigitalInOut(board.GP19)
s1.direction = digitalio.Direction.INPUT
s1.pull = digitalio.Pull.DOWN


n=0
while True:
    #print(break_beam.value)
    n+=1
    print(n, s1.value,)
    time.sleep(0.1)


