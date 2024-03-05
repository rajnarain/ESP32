from machine import Pin 
from time import sleep 
led = Pin(15, Pin.OUT) 
button = Pin(2, Pin.IN, Pin.PULL_UP) 
while True: 
    led.value(button.value())
    print(button.value())
    sleep(0.1) 
