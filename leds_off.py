# This script will switch off any neopixels still switched on:

# This file was created on 31/01/17
# Author: George Kaimakis


import machine
import neopixel


PIXEL_PIN       = 0
PIXEL_WIDTH     = 4
PIXEL_HEIGHT    = 4



# Initiallize neopixels:
np = neopixel.NeoPixel(machine.Pin(PIXEL_PIN), PIXEL_WIDTH * PIXEL_HEIGHT)
np.fill((0,0,0))
np.write()
