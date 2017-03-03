# This short program turns off the built-in led:

# This file was created on 02/03/2017
# Author: George Kaimakis


import machine
import time

# led set-up:
PIXEL_PIN       = 16

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)
led.high()
