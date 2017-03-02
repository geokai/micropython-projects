# This short program utilizes the built-in blue LED on the Node-MCU board:
# The LED is flashed on and off within an infinite loop:

# This file was created on 02/03/2017
# Author: George Kaimakis


import machine
import time
import neopixel

# led set-up:
PIXEL_PIN       = 16
INTERVAL        = 0.5

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)

while True:
    led.low()
    time.sleep(INTERVAL)
    led.high()
    time.sleep(INTERVAL)
