"""simple led flash script as a verification the board is operational"""

from time import sleep_ms
from machine import Pin

led = Pin(2, Pin.OUT)

def blink(interval, cnt):
    """blink the led for 'cnt' times, for 'interval' milliseconds"""
    for x in range(cnt):
        led.value(0)
        sleep_ms(interval)
        led.value(1)
        sleep_ms(interval)

blink(500, 4)
print()
print("Hello World!")
for i in range(1, 11):
    sleep_ms(250)
    print(i)
print()
sleep_ms(250)

while True:
    print('Flash!')
    blink(250, 1)
