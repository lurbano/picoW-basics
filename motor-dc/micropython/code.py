# Ref: https://microcontrollerslab.com/dc-motor-l298n-driver-raspberry-pi-pico-tutorial/

from machine import Pin, PWM
from time import sleep

IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

speed = PWM(Pin(4))
speed.freq(1000)

while True:
        speed.duty_u16(10000)
        IN1.low()  #spin forward
        IN2.high()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        speed.duty_u16(20000)
        IN1.high()  #spin backward
        IN2.low()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
    
        speed.duty_u16(30000)
        IN1.low()  #spin forward
        IN2.high()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        speed.duty_u16(40000)
        IN1.high()  #spin backward
        IN2.low()
        sleep(5)