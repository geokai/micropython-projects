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

INTERVAL = 400   # blinkin' frequency:

while True:
    oled.framebuf.fill_rect(0, 0, 128, 16, 1)   # upper 'yellow' area filled:
    oled.framebuf.fill_rect(0, 16, 128, 48, 0)  # lower 'blue' area:
    oled.framebuf.rect(0, 16, 128, 48, 1)       # lower 'blue' area:
    oled.show()
    time.sleep_ms(INTERVAL)
    oled.framebuf.fill_rect(0, 0, 128, 16, 0)   # upper 'yellow' area:
    oled.framebuf.rect(0, 0, 128, 16, 1)        # upper 'yellow' area:
    oled.framebuf.fill_rect(0, 16, 128, 48, 1)  # lower 'blue' area filled:
    oled.show()
    time.sleep_ms(INTERVAL)

