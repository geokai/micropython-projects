import neopixel
import machine
from time import sleep_ms


pix = neopixel.NeoPixel(machine.Pin(12, machine.Pin.OUT), 1)

pix.fill((0, 0, 0))
pix.write()
