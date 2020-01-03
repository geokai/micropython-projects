import machine
import neopixel
from time import sleep_ms


pix = neopixel.NeoPixel(machine.Pin(12, machine.Pin.OUT), 1)


def colors_cycle():
    while True:
        pix[0] = (128, 0, 0)
        pix.write()
        sleep_ms(250)
        pix[0] = (255, 0, 0)
        pix.write()
        sleep_ms(250)
        pix[0] = (128, 128, 0)
        pix.write()
        sleep_ms(250)
        pix[0] = (0, 255, 0)
        pix.write()
        sleep_ms(250)
        pix[0] = (0, 128, 128)
        pix.write()
        sleep_ms(250)
        pix[0] = (0, 0, 255)
        pix.write()
        sleep_ms(250)
        pix[0] = (128, 0, 128)
        pix.write()
        sleep_ms(250)


colors_cycle()
