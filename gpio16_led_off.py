"""this short script sets the led value to 1, (active low) turning led off

The api for Pin objects has been changed from using 'high()' & 'low()'
to 'on()' & 'off()' making things confusing with active low implementations.
For this I'm using 'value(0|1)' method to hopefully make things clearer.
"""

# This file was created on 02/03/2017
# Author: George Kaimakis


import time
import machine

# led set-up:
PIXEL_PIN = 16

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)
led.value(1)    # active-low, 0 = on, 1 = off
