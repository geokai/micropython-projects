"""This script uses the BME280 sensor to return temperature, atmospheric pressure
and humidity.
Uses a one-wire method of connection to the device on the ESP8266 using
a software i2c method:
"""

# Micropython implementation for the ESP8266:
# (Adapt as necessary for your chosen platform)

# This file was created on 30/03/2017
# Author: George Kaimakis


from time import sleep
import machine
import bme280

BOARD_LED = 16  # on-board led used as 'reading sensor' indicator:
INTERVAL = 10   # interval between readings (loop):
PAUSE = 0.5     # small pause before printing results (for effect!):
BLIP = 0.05     # tiny delay for the led indicator:


# create objects for i2c and the bme280 sensor:
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

# create led indicator object:
led = machine.Pin(BOARD_LED, machine.Pin.OUT)

# print the device id before entering the loop:
print()
print('i2c devices found: {0}'.format(i2c.scan()))
print()


def led_flash():
    """momentary 'blip' of the led to indicate sensor reading taken"""
    led.value(0)    # active low, 0 = on
    sleep(BLIP)
    led.value(1)    # active low, 1 = off


counter = 0     # reset counter:

# main loop:
while True:
    print("Checking", end='')
    led_flash()
    readings = bme.read_compensated_data()
    sleep(PAUSE)
    for i in range(3):
        print('.', end='')
        sleep(PAUSE)
    print("\rTemperature, Pressure & Humidity ...{0}".format(counter + 1))
    sleep(PAUSE)
    # Adjustment factors for aquired readings (refer to bme280 datasheet):
    print("Temp:  \t{0:6.1f} Celcius".format(readings[0]/100))
    print("Pres: \t{0:6.1f} hPa/mb".format(readings[1]/256/100))
    print("Humi: \t{0:6.1f} % RH".format(readings[2]/1024))
    print()
    counter += 1        # increment counter:
    sleep(INTERVAL)     # loop cycle:
