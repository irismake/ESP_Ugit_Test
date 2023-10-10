import machine

import time

led = machine.Pin(2,machine.Pin.OUT)

for i in range(10):
    led.value(1)
    time.sleep(.5)
    led.value(0)
    time.sleep(.5)