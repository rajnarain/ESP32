from machine import Pin 
from time import sleep 
led = Pin(15, Pin.OUT) 
while True:       #for repeated loop
    led.value(1) 
    sleep(2)
    led.value(0) 
    sleep(2) 
 

