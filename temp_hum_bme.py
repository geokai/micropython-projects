# This script uses the BME280 sensor to return temperature and humidity.
# Uses a one-wire method of connection to the device:

# This file was created on 30/03/2017
# Author: George Kaimakis


import machine
import bme280
from time import sleep

PIXEL_PIN   = 16    # used as 'reading sensor' indicator:
INTERVAL    = 10    # delay between readings:
PAUSE       = 0.5   # small pause before printing results (for effect!):
BLIP        = 0.05  # tiny delay for the led indicator:

# create objects for i2c and the bme280 sensor:
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

led = machine.Pin(PIXEL_PIN, machine.Pin.OUT)

# print the device id before entering the loop:
print()
print('sensor id {0}'.format(i2c.scan()))
print()

counter = 0     # reset counter:

while True:
    print("Checking Temp, Pressure & Humidity ...{0}".format(counter + 1))
    #print()
    readings = bme.read_compensated_data()
    led.low()
    sleep(BLIP)
    led.high()
    sleep(PAUSE)
    print("Temperature  \t{0:6.1f} Celcius".format(readings[0]/100))
    print("Pressure \t{0:6.1f} hPa".format(readings[1]/256/100))
    print("Humidity \t{0:6.1f} % RH".format(readings[2]/1024))
    print()
    counter += 1    # increment counter:
    sleep(INTERVAL)
