"""Blink the built-in led at 'INTERVAL' rate

Note the use of 'value()' instead of 'on()' & 'off()' methods to avoid
confusion with active low pins.
"""

# This short program utilizes the built-in blue LED on the Node-MCU board:
# The LED is flashed on and off within an infinite loop:

# This file was created on 02/03/2017
# Author: George Kaimakis


import time
import machine
import neopixel

# led set-up:
PIXEL_PIN = 16
INTERVAL = 0.5

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(INTERVAL)
    led.value(0)
    time.sleep(INTERVAL)
