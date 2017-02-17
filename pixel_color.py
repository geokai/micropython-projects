# This script provides a means to test for different colors using
# the neopixel

# This file was created on 31/01/17
# Author: George Kaimakis


import machine
import time
import neopixel


# neopixel set-up:
PIXEL_PIN       = 0
PIXEL_WIDTH     = 1
PIXEL_HEIGHT    = 1
PIXEL_COUNT     = 15

INTERVAL        = 1000

# color values:
R               = 254
G               = 60
B               = 70

c1              = (254,183,12)
c2              = (255,255,0)


# Initiallize and blank neopixels:
np = neopixel.NeoPixel(machine.Pin(PIXEL_PIN), PIXEL_COUNT)
np.fill((0,0,0))
np.write()
time.sleep_ms(500)

while True:
    np[10] = (c1)
    np.write()
    time.sleep_ms(INTERVAL)
    np[5] = (c2)
    np.write()
    time.sleep_ms(INTERVAL)
