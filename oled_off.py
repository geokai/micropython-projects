# This script uses the ssd1306 oled module.
# to switch off all display pixels:

# This file was created on 15/04/2017
# Author: George Kaimakis

import machine
import ssd1306

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

oled.fill(0)
oled.show()
