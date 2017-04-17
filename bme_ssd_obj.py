# Micropython implementation for the ESP8266:
# (Adapt as necessary for your chosen platform)

# This script creates ssd1306 and bme280 objects for debugging purposes,
# the intention is to then use the REPL to perform tests for these two devices:

# This file was created on 17/04/2017
# Author: George Kaimakis


# general modules:
import machine
import time

# device modules:
import bme280
import ssd1306

# define i2c pins:
data    = machine.Pin(4)
clk     = machine.Pin(5)

# create i2c object:
i2c = machine.I2C(scl=clk, sda=data)

# define the display size:
width   = 128   # pixels
height  = 64    # pixels

# create oled object:
oled = ssd1306.SSD1306_I2C(width, height, i2c)

# create a bme280 object:
bme = bme280.BME280(i2c=i2c)

# return i2c devices id:
devices = i2c.scan()
print()
print('i2c devices found: {0}'.format(devices))
print()
