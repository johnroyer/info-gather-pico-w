# demo code from:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6

from machine import Pin, Timer
led = Pin(15, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
