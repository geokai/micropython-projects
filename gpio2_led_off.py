"""This short script truns off the (pwm) built-in les (2)

Using 'value()' instead of 'on()' & 'off()' to avoid confusion with
active low pins
"""

# This file was created on 02/03/2017
# Author: George Kaimakis


import time
import machine

# led set-up:
PIXEL_PIN = 2

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)
led.value(1)    # active low pin, 0 = on, 1 = off
