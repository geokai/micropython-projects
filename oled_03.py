# This script uses the ssd1306 oled module:

# This file was created on 15/04/2017
# Author: George Kaimakis

import machine
import ssd1306
import time

# define the display size:
width   = 128   # pixels
height  = 64    # pixels

# define i2c pins:
data    = machine.Pin(4)
clk     = machine.Pin(5)

# create i2c object:
i2c = machine.I2C(scl=clk, sda=data)

#create oled object:
oled = ssd1306.SSD1306_I2C(width, height, i2c)

# blank the display:
oled.fill(0)
oled.show()
time.sleep_ms(500)

# the framebuf class contains methods for drawing rectangles
# fill_rect, rect - also use these with height/width of 1 pixel to create lines:

while True:

    oled.framebuf.rect(0, 32, 1, 20,  1)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(32, 32, 1, 20,  1)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(64, 32, 1, 20,  1)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(96, 32, 1, 20,  1)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(127, 32, 1, 20,  1)
    oled.show()

    time.sleep_ms(500)

    oled.framebuf.rect(0, 32, 1, 20,  0)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(32, 32, 1, 20,  0)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(64, 32, 1, 20,  0)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(96, 32, 1, 20,  0)
    oled.show()
    time.sleep_ms(500)
    oled.framebuf.rect(127, 32, 1, 20,  0)
    oled.show()
    time.sleep_ms(500)
