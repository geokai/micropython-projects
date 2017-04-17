# Micropython implementation for the ESP8266:
# (Adapt as necessary for your chosen platform)

# This script uses the BME280 sensor to return temperature, atmospheric pressure
# and humidity.
# Uses a one-wire method of connection to the device on the ESP8266 using
# a software i2c method:

# This file was created on 30/03/2017
# Author: George Kaimakis


import machine
import bme280
from time import sleep

PIXEL_PIN   = 16    # used as 'reading sensor' indicator:
INTERVAL    = 10    # interval between readings:
PAUSE       = 0.5   # small pause before printing results (for effect!):
BLIP        = 0.05  # tiny delay for the led indicator:


# create objects for i2c and the bme280 sensor:
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)

# print the device id before entering the loop:
print()
print('i2c devices found: {0}'.format(i2c.scan()))
print()


def led_flash():
    led.low()
    sleep(BLIP)
    led.high()


# aquire readings from bme280 sensor:
readings = bme.read_compensated_data()

# Adjustment factors for aquired readings (refer to bme280 datasheet):
temp_factor     = readings[0]/100       # temerature:
press_factor    = readings[1]/256/100   # barometric pressure:
humi_factor     = readings[2]/1024      # relative humidity:

counter = 0     # reset counter:

# main loop:
while True:
    print("Checking...", end='')
    sleep(PAUSE)
    print("\rTemperature, Pressure & Humidity ...{0}".format(counter + 1))
    led_flash()
    sleep(PAUSE)
    print("Temp:  \t{0:6.1f} Celcius".format(temp_factor))
    print("Pres: \t{0:6.1f} hPa/mb".format(press_factor))
    print("Humi: \t{0:6.1f} % RH".format(humi_factor))
    print()
    counter += 1    # increment counter:
    sleep(INTERVAL)
